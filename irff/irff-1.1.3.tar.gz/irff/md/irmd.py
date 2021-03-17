#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argh
import argparse
from ..irff import IRFF
from ..AtomDance import get_zmat_variable,get_zmat_angle,get_zmatrix,check_zmat
from ase.io import read,write
import numpy as np
from ase.optimize import BFGS
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.io.trajectory import Trajectory
from ase import units


def fvr(x):
    xi  = np.expand_dims(x,axis=0)
    xj  = np.expand_dims(x,axis=1) 
    vr  = xj - xi
    return vr


def fr(vr):
    R   = np.sqrt(np.sum(vr*vr,axis=2))
    return R


def getBonds(natom,r,rcut):
    bonds = [] 
    for i in range(natom-1):
        for j in range(i+1,natom):
            if r[i][j]<rcut[i][j]:
               bonds.append((i,j))
    return bonds


class IRMD(object):
  ''' Intelligent Reactive Molecular Dynamics '''
  def __init__(self,label=None,atoms=None,gen='poscar.gen',ffield='ffield.json',
               index=-1,totstep=100,vdwnn=False,nn=True,
               initT=300,Tmax=10000,time_step=0.1,Iter=0,
               ro=None,rmin=0.6,rmax=1.3,angmax=20.0,
               UseZmat=False,zmat_id=None,zmat_index=None,InitZmat=None,
               dEstop=0.5):
      self.Epot    = []
      self.epot    = 0.0
      self.ekin    = 0.0
      self.T       = 0.0
      self.initT   = initT
      self.Tmax    = Tmax
      self.totstep = totstep
      self.ro      = ro
      self.rmin    = rmin
      self.Iter    = Iter
      self.atoms   = atoms
      self.time_step = time_step
      self.step    = 0
      self.rmax    = rmax
      self.angmax  = angmax
      self.UseZmat = UseZmat
      self.zmat_id   = zmat_id
      self.zmat_index= zmat_index
      self.InitZmat  = InitZmat
      self.zmats     = []
      self.dEstop    = dEstop

      if self.atoms is None:
         self.atoms  = read(gen,index=index)
      
      self.atoms.calc= IRFF(atoms=self.atoms, mol=label,libfile=ffield,
                             rcut=None,nn=nn,vdwnn=vdwnn)
      self.natom     = len(self.atoms)
      self.re        = self.atoms.calc.re
      self.dyn       = None
      self.atoms.calc.calculate(atoms=self.atoms)
      self.InitBonds = getBonds(self.natom,self.atoms.calc.r,self.rmax*self.re)

      if (self.atoms is None) and gen.endswith('.gen'):
         MaxwellBoltzmannDistribution(self.atoms, self.initT*units.kB)
      else:
         temp = self.atoms.get_temperature()
         if temp>0.0000001:
            scale = np.sqrt(self.initT/temp)
            p    = self.atoms.get_momenta()
            p    = scale * p
            self.atoms.set_momenta(p)
         else:
            MaxwellBoltzmannDistribution(self.atoms, self.initT*units.kB)

  def run(self):
      self.zv,self.zvlo,self.zvhi = None,0.0,0.0
      self.dyn = VelocityVerlet(self.atoms, self.time_step*units.fs,trajectory='md.traj')  
      def printenergy(a=self.atoms):
          epot_      = a.get_potential_energy()
          n,self.Deformed = 0,0
          if self.UseZmat:
             self.Deformed,zmat,self.zv,self.zvlo,self.zvhi = check_zmat(atoms=a,rmin=self.rmin,rmax=self.rmax,
                                             angmax=self.angmax,zmat_id=self.zmat_id,
                                             zmat_index=self.zmat_index,InitZmat=self.InitZmat)
             bonds      = getBonds(self.natom,self.atoms.calc.r,1.22*self.re)
             newbond    = self.checkBond(bonds)
             if newbond: 
                self.zv = None
                self.Deformed += 0.2
                bonds      = getBonds(self.natom,self.atoms.calc.r,1.25*self.re)
                newbond    = self.checkBond(bonds)
                if newbond: 
                   self.Deformed += 0.2
                   bonds      = getBonds(self.natom,self.atoms.calc.r,1.23*self.re)
                   newbond    = self.checkBond(bonds)
                   if newbond: 
                      self.Deformed += 0.2
                      bonds      = getBonds(self.natom,self.atoms.calc.r,1.21*self.re)
                      newbond    = self.checkBond(bonds)
                      if newbond: 
                         self.Deformed += 0.2
                         bonds      = getBonds(self.natom,self.atoms.calc.r,1.19*self.re)
                         newbond    = self.checkBond(bonds)
                         if newbond: 
                            self.Deformed += 0.2
                            bonds      = getBonds(self.natom,self.atoms.calc.r,1.17*self.re)
                            newbond    = self.checkBond(bonds)
             self.zmats.append(zmat)
          else:
             r        = a.calc.r.detach().numpy()
             i_       = np.where(np.logical_and(r<self.rmin*self.ro,r>0.0001))
             n        = len(i_[0])

          if len(self.Epot)==0:
             dE_ = 0.0
          else:
             dE_ = abs(epot_ - self.Epot[-1])
          self.Epot.append(epot_)

          self.epot  = epot_/self.natom
          self.ekin  = a.get_kinetic_energy()/self.natom
          self.T     = self.ekin/(1.5*units.kB)
          self.step  = self.dyn.nsteps

          print('Step %d Epot = %.3feV  Ekin = %.3feV (T=%3.0fK)  '
                'Etot = %.3feV' % (self.step,self.epot,self.ekin,self.T,
                                   self.epot + self.ekin))
          try:
             if self.UseZmat:
                assert self.Deformed<1,'Atoms structure is deformed!' 
             else:
                assert n==0 and self.T<self.Tmax,'Atoms too closed or Temperature goes too high!' 
          except:
             # for _ in i_:
             #     print('atoms pair',_)
             if n>0: 
                 print('Atoms too closed, stop at %d.' %self.step)
             elif self.Deformed>=1.0: 
                 print('Structure Deformed = %f exceed the limit, stop at %d.' %(self.Deformed,self.step))
             else:
                 print('unknown reason, stop at %d.' %self.step)
             self.dyn.max_steps = self.dyn.nsteps-1
  
      # traj = Trajectory('md.traj', 'w', self.atoms)
      self.dyn.attach(printenergy,interval=1)
      # self.dyn.attach(traj.write,interval=1)
      self.dyn.run(self.totstep)
      return self.Deformed,self.zmats,self.zv,self.zvlo,self.zvhi

  def opt(self):
      self.zv,self.zvlo,self.zvhi = None,0.0,0.0
      self.dyn = BFGS(self.atoms,trajectory='md.traj')
      def check(a=self.atoms):
          epot_      = a.get_potential_energy()
          n,self.Deformed = 0,0
          if self.UseZmat:
             Deformed,zmat,self.zv,self.zvlo,self.zvhi = check_zmat(atoms=a,rmin=self.rmin,rmax=self.rmax,angmax=self.angmax,
                                        zmat_id=self.zmat_id,zmat_index=self.zmat_index,
                                        InitZmat=self.InitZmat)
             bonds      = getBonds(self.natom,self.atoms.calc.r,1.18*self.re)
             newbond    = self.checkBond(bonds)
             if newbond: 
                self.zv = None
                self.Deformed += 0.2
                bonds      = getBonds(self.natom,self.atoms.calc.r,1.25*self.re)
                newbond    = self.checkBond(bonds)
                if newbond: 
                   self.Deformed += 0.2
                   bonds      = getBonds(self.natom,self.atoms.calc.r,1.23*self.re)
                   newbond    = self.checkBond(bonds)
                   if newbond: 
                      self.Deformed += 0.2
                      bonds      = getBonds(self.natom,self.atoms.calc.r,1.21*self.re)
                      newbond    = self.checkBond(bonds)
                      if newbond: 
                         self.Deformed += 0.2
                         bonds      = getBonds(self.natom,self.atoms.calc.r,1.19*self.re)
                         newbond    = self.checkBond(bonds)
                         if newbond: 
                            self.Deformed += 0.2
                            bonds      = getBonds(self.natom,self.atoms.calc.r,1.17*self.re)
                            newbond    = self.checkBond(bonds)
             self.zmats.append(zmat)
          else:
             r          = a.calc.r.detach().numpy()
             i_         = np.where(np.logical_and(r<self.rmin*self.ro,r>0.0001))
             n          = len(i_[0])
          
          self.Epot.append(epot_)
          self.epot  = epot_/self.natom

          self.step  = self.dyn.nsteps
          try:
             if self.UseZmat:
                assert Deformed<1,'Atoms too closed or Deformed!' 
             else:
                assert n==0 and (not np.isnan(epot_)),'Atoms too closed!'
          except:
             if n>0: 
                 print('Atoms too closed, stop at %d.' %self.step)
             elif self.Deformed>=1.0: 
                 print('Structure Deformed = %f exceed the limit, stop at %d.' %(self.Deformed,self.step))
             elif np.isnan(epot_):
                 print('potential energy is NAN, stop at %d.' %self.step)
             else:
                 print('unknown reason, stop at %d.' %self.step)
             self.dyn.max_steps = self.dyn.nsteps-1
  
      self.dyn.attach(check,interval=1)
      self.dyn.run(0.00001,self.totstep)
      return self.Deformed,self.zmats,self.zv,self.zvlo,self.zvhi

  def checkBond(self,bonds):
      newbond = False
      for bd in bonds:
          bd_ = (bd[1],bd[0])
          if (bd not in self.InitBonds) and (bd_ not in self.InitBonds):
             newbond = True
             return newbond 
      return newbond

  def logout(self):
      with open('md.log','w') as fmd:
         fmd.write('\n------------------------------------------------------------------------\n')
         fmd.write('\n-       Energies From Machine Learning MD Iteration %4d               -\n' %self.Iter)
         fmd.write('\n------------------------------------------------------------------------\n')

         fmd.write('-  Ebond=%f  ' %self.atoms.calc.Ebond)
         fmd.write('-  Elone=%f  ' %self.atoms.calc.Elone)
         fmd.write('-  Eover=%f  ' %self.atoms.calc.Eover)
         fmd.write('-  Eunder=%f  \n' %self.atoms.calc.Eunder)
         fmd.write('-  Eang=%f  ' %self.atoms.calc.Eang)
         fmd.write('-  Epen=%f  ' %self.atoms.calc.Epen)
         fmd.write('-  Etcon=%f  \n' %self.atoms.calc.Etcon)
         fmd.write('-  Etor=%f  ' %self.atoms.calc.Etor)
         fmd.write('-  Efcon=%f  ' %self.atoms.calc.Efcon)
         fmd.write('-  Evdw=%f  ' %self.atoms.calc.Evdw)
         fmd.write('-  Ecoul=%f  \n' %self.atoms.calc.Ecoul)
         fmd.write('-  Ehb=%f  ' %self.atoms.calc.Ehb)
         fmd.write('-  Eself=%f  ' %self.atoms.calc.Eself)
         fmd.write('-  Ezpe=%f \n' %self.atoms.calc.zpe)
         
         fmd.write('\n------------------------------------------------------------------------\n')
         fmd.write('\n-              Atomic Information  (Delta and Bond order)              -\n')
         fmd.write('\n------------------------------------------------------------------------\n')
         fmd.write('\n  AtomID Sym  Delta      NLP      DLPC      Bond-Order  \n')

         for i in range(self.natom):
             fmd.write('%6d  %2s %9.6f %9.6f %9.6f' %(i,
                                      self.atoms.calc.atom_name[i],
                                      self.atoms.calc.Delta[i],
                                      self.atoms.calc.nlp[i],
                                      self.atoms.calc.Delta_lpcorr[i]))
             for j in range(self.natom):
                   if self.atoms.calc.bo0[i][j]>self.atoms.calc.botol:
                      fmd.write(' %3d %2s %9.6f' %(j,self.atoms.calc.atom_name[j],
                                                 self.atoms.calc.bo0[i][j]))
             fmd.write(' \n')

         fmd.write('\n------------------------------------------------------------------------\n')
         fmd.write('\n-                    Atomic Energies & Forces                          -\n')
         fmd.write('\n------------------------------------------------------------------------\n')

         fmd.write('\n  AtomID Sym Delta_lp     Elone      Eover      Eunder      Fx        Fy        Fz\n')
         for i in range(self.natom):
             fmd.write('%6d  %2s  %9.6f  %9.6f  %9.6f  %9.6f ' %(i,
                       self.atoms.calc.atom_name[i],
                       self.atoms.calc.Delta_lp[i],
                       self.atoms.calc.elone[i],
                       self.atoms.calc.eover[i],
                       self.atoms.calc.eunder[i]))

             for f in self.atoms.calc.results['forces'][i]:
                   fmd.write(' %9.6f ' %f)
             fmd.write(' \n')

         fmd.write('\n------------------------------------------------------------------------\n')
         fmd.write('\n- Machine Learning MD Completed!\n')

  def close(self):
      self.logout()
      self.dyn   = None
      self.atoms = None


if __name__ == '__main__':
   ''' use commond like ./irmd.py md --T=2800 to run it'''
   parser = argparse.ArgumentParser()
   argh.add_commands(parser, [md])
   argh.dispatch(parser)

   
