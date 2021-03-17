#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD.
# See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#
# Main author and maintainer: Ask Hjorth Larsen <asklarsen@gmail.com>

varlist = [
    '%endblock',
    'Atom-Setup-Only',
    'Atom.Debug.KB.Generation',
    'AtomCoorFormatOut',
    'AtomLeftVcte',
    'AtomRightVcte',
    'AtomicCoordinatesFormat',
    'BasisPressure',
    'BornCharge',
    'BuildSuperCell',
    'BulkLead',
    'BulkTransport',
    'BulkTransvCellSize',
    'BulkTransvCellSizeX',
    'BulkTransvCellSizeY',
    'BulkTransvCellSizeZ',
    'CB.MaxKappa',
    'CB.WriteComplexBands',
    'CDFT',
    'CDFT.MaxIter',
    'COOP.Write',
    'CalcIETS',
    'CalcMPSH',
    'ChangeKgridInMD',
    'Compat-pre-v4-DM-H',
    'DM.AllowExtrapolation',
    'DM.AllowReuse',
    'DM.EnergyTolerance',
    'DM.FIRE.Mixing',
    'DM.FormattedFiles',
    'DM.FormattedInput',
    'DM.FormattedOutput',
    'DM.HarrisTolerance',
    'DM.KickMixingWeight',
    'DM.MixSCF1',
    'DM.MixingWeight',
    'DM.NormalizationTolerance',
    'DM.NormalizeDuringSCF',
    'DM.NumberBroyden',
    'DM.NumberKick',
    'DM.NumberPulay',
    'DM.OccupancyTolerance',
    'DM.Pulay.Avoid.First.After.Kick',
    'DM.PulayOnFile',
    'DM.RequireEnergyConvergence',
    'DM.RequireHarrisConvergence',
    'DM.Tolerance',
    'DM.UseSaveDM',
    'Delta',
    'DeltaWorkfunction',
    'Diag.AllInOne',
    'Diag.DivideAndConquer',
    'Diag.Memory',
    'Diag.NoExpert',
    'Diag.ParallelOverK',
    'Diag.PreRotate',
    'Diag.Use2D',
    'DiagMemory',
    'DiagScale',
    'DirectPhi',
    'DivideAndConquer',
    'EM.AddRhoGate',
    'EM.AddVgIsolatedLocalCharges',
    'EM.COOPCalculate',
    'EM.COOPNumberOfBonds',
    'EM.DebugRhoGate',
    'EM.NetRhoGateCharge',
    'EM.PrintLimits',
    'EM.RhoGateLxMax',
    'EM.RhoGateLxMin',
    'EM.RhoGateLyMax',
    'EM.RhoGateLyMin',
    'EM.RhoGateLzMax',
    'EM.RhoGateLzMin',
    'EM.TRCAddVCDFT',
    'EM.TimeReversal',
    'EM.Timings',
    'EM.addV',
    'EMPDOSKSO',
    'EMTransport',
    'ElectronicTemperature',
    'EnergLowestBound',
    'FilterCutoff',
    'FilterTol',
    'FinalTransmRange',
    'FixAuxiliaryCell',
    'FixAuxillaryCell',
    'FixSpin',
    'ForceAuxCell',
    'FullRamp',
    'HSetupOnly',
    'Harris_functional',
    'HartreeLeadsBottom',
    'HartreeLeadsLeft',
    'HartreeLeadsRight',
    'Ik_Select',
    'InitTransmRange',
    'InitTransport',
    'KB.New.Reference.Orbitals',
    'KB.Rmax',
    'LDAU.units',
    'LDAUForces',
    'LDAU_METHOD',
    'LatticeConstant',
    'LongOutput',
    'MD.AnnealOption',
    'MD.BulkModulus',
    'MD.FCAcousticSumRule',
    'MD.FCAtomRestart',
    'MD.FCAxisRestart',
    'MD.FCDispl',
    'MD.FCEigenVectors',
    'MD.FCIR',
    'MD.FCRead',
    'MD.FCfirst',
    'MD.FClast',
    'MD.FinalTimeStep',
    'MD.FireQuench',
    'MD.InitialTemperature',
    'MD.InitialTimeStep',
    'MD.LengthTimeStep',
    'MD.MaxCGDispl',
    'MD.MaxForceTol',
    'MD.MaxStressTol',
    'MD.NoseMass',
    'MD.NumCGsteps',
    'MD.NumNEBsteps',
    'MD.ParrinelloRahmanMass',
    'MD.Quench',
    'MD.RelaxCellOnly',
    'MD.RemoveIntraMolecularPressure',
    'MD.TRCSampling',
    'MD.TRCSkip',
    'MD.TargetPressure',
    'MD.TargetTemperature',
    'MD.TauRelax',
    'MD.Timing',
    'MD.TypeOfRun',
    'MD.UseSaveCG',
    'MD.UseSaveNEB',
    'MD.UseSaveXV',
    'MD.UseSaveZM',
    'MD.UseStructFile',
    'MD.VariableCell',
    'MM.Cutoff',
    'MM.UnitsDistance',
    'MM.UnitsEnergy',
    'MPSHAtomFirst',
    'MPSHAtomLast',
    'MPSHOrbFirst',
    'MPSHOrbLast',
    'MaxBondDistance',
    'MaxSCFIterations',
    'MeshCutoff',
    'MeshSubDivisions',
    'MinSCFIterations',
    'MixCharge',
    'MixHamiltonian',
    'MixedParallel',
    'MonitorForcesInSCF',
    'MullikenInSCF',
    'NC.OrbitalRotationEnd',
    'NC.OrbitalRotationStart',
    'NEB.SkipEdge',
    'NEnergReal',
    'NIVPoints',
    'NPoles',
    'NSlices',
    'NTransmPoints',
    'NaiveAuxiliaryCell',
    'NeglNonOverlapInt',
    'NenergImCircle',
    'NenergImLine',
    'NetCharge',
    'NonCollinearSpin',
    'NumSkipWriteDM',
    'NumberLinearMix',
    'NumberOfAtoms',
    'NumberOfEigenStates',
    'NumberOfSpecies',
    'Number_of_species',
    'ON.ChemicalPotential',
    'ON.ChemicalPotentialOrder',
    'ON.ChemicalPotentialRc',
    'ON.ChemicalPotentialTemperature',
    'ON.ChemicalPotentialUse',
    'ON.MaxNumIter',
    'ON.UseSaveLWF',
    'ON.eta',
    'ON.eta_alpha',
    'ON.eta_beta',
    'ON.etol',
    'ON.functional',
    'OccupationFunction',
    'On.RcLWF',
    'OpticalCalculation',
    'Optim.Broyden',
    'Output-Structure-Only',
    'PAO.BasisSize',
    'PAO.BasisType',
    'PAO.EnergyShift',
    'PAO.Filter',
    'PAO.FixSplitTable',
    'PAO.Keep.Findp.Bug',
    'PAO.NewSplitCode',
    'PAO.OldStylePolorbs',
    'PAO.SoftDefault',
    'PAO.SoftInnerRadius',
    'PAO.SoftPotential',
    'PAO.SplitNorm',
    'PAO.SplitNormH',
    'PAO.SplitTailNorm',
    'PS.SIC',
    'ParallelOverK',
    'PartialChargesAtEveryGeometry',
    'PartialChargesAtEveryScfStep',
    'PoissonMultigrid',
    'Print_ldau',
    'ProcessorGridX',
    'ProcessorGridY',
    'ProcessorGridZ',
    'ProjectionInSCF',
    'ProjectionMethod',
    'RcSpatial',
    'ReInitialiseDM',
    'ReadHamiltonian',
    'ReadKPIN',
    'ReparametrizePseudos',
    'Restricted.Radial.Grid',
    'Rmax.Radial.Grid',
    'RotateSpin.Phi',
    'RotateSpin.Theta',
    'SCF.LinearMixingAfterPulay',
    'SCF.MixAfterConvergence',
    'SCF.MixingWeightAfterPulay',
    'SCF.Pulay.Damping',
    'SCF.Pulay.DebugSVD',
    'SCF.Pulay.RcondSVD',
    'SCF.Pulay.UseSVD',
    'SCF.PulayDmaxRegion',
    'SCF.PulayMinimumHistory',
    'SCF.Read.Charge.NetCDF',
    'SCF.Read.Deformation.Charge.NetCDF',
    'SCF.Recompute-H-After-Scf',
    'SCF.Want.Variational.EKS',
    'SCFMustConverge',
    'SIC.Flavour',
    'SIC.Lambda',
    'SIC.NoRelaxation',
    'SIC.Npop',
    'SIC.PopDMConv',
    'SIC.PopKgridFactor',
    'SIC.PopSmatSparsity',
    'SIC.ProjectionMode',
    'SIC.ProjectionType',
    'SIC.Rot_Inv',
    'STT.Calculation',
    'STT.LinearResponse',
    'SaveBaderCharge',
    'SaveDeltaRho',
    'SaveElectrostaticPotential',
    'SaveHS',
    'SaveInitialChargeDensity',
    'SaveIonicCharge',
    'SaveNeutralAtomPotential',
    'SaveRho',
    'SaveRhoXC',
    'SaveTotalCharge',
    'SaveTotalPotential',
    'Scissor.Operator',
    'SetBulkTransvCell',
    'Siesta2Wannier90.NumberOfBands',
    'Siesta2Wannier90.NumberOfBandsDown',
    'Siesta2Wannier90.NumberOfBandsUp',
    'Siesta2Wannier90.WriteAmn',
    'Siesta2Wannier90.WriteEig',
    'Siesta2Wannier90.WriteMmn',
    'Siesta2Wannier90.WriteUnk',
    'Sigma.DSigmaDE',
    'SignatureRecords',
    'SimulateDoping',
    'SingleExcitation',
    'SkipLastIter',
    'SlabDipoleCorrection',
    'SolutionMethod',
    'SpinConfLeads',
    'SpinOrbit',
    'SpinPolarized',
    'SystemLabel',
    'SystemName',
    'TS.MixH',
    'TimeReversal',
    'TimeReversalSymmetryForKpoints',
    'TrCoefficients',
    'TryMemoryIncrease',
    'UseDomainDecomposition',
    'UseNewDiagk',
    'UseSaveData',
    'UseSpatialDecomposition',
    'UseStructFile',
    'UseTreeTimer',
    'VFinal',
    'VGate',
    'VInitial',
    'Vna.Filter',
    'WarningMinimumAtomicDistance',
    'WriteBands',
    'WriteCoorCerius',
    'WriteCoorInitial',
    'WriteCoorStep',
    'WriteCoorXmol',
    'WriteDM',
    'WriteDM.History.NetCDF',
    'WriteDM.NetCDF',
    'WriteDMHS.History.NetCDF',
    'WriteDMHS.NetCDF',
    'WriteDMT',
    'WriteDenchar',
    'WriteDiagdS',
    'WriteEDM',
    'WriteEigenvalues',
    'WriteForces',
    'WriteHSDeriv',
    'WriteHamiltonPop',
    'WriteHirshfeldPop',
    'WriteIonPlotFiles',
    'WriteKbands',
    'WriteKpoints',
    'WriteMDXmol',
    'WriteMDhistory',
    'WriteMullikenPop',
    'WriteProjections',
    'WriteSpinMulliken',
    'WriteSpinSCF',
    'WriteVNA',
    'WriteVoronoiPop',
    'WriteWaveFunctions',
    'XML.AbortOnErrors',
    'XML.AbortOnWarnings',
    'XML.Write',
    'ZBroadeningG',
    'ZLeftVcte',
    'ZM.CalcAllForces',
    'ZM.ForceTolAngle',
    'ZM.ForceTolLength',
    'ZM.MaxDisplAngle',
    'ZM.MaxDisplLength',
    'ZM.UnitsAngle',
    'ZM.UnitsLength',
    'ZRightVcte',
    'ZVGateL',
    'ZVGateR',
    'ZeemanTermBx',
    'ZeemanTermBy',
    'ZeemanTermBz',
    'alloc_report_level',
    'alloc_report_threshold',
    'blocksize',
    'compat-pre-v4-dynamics',
    'fdf-debug',
    'kgrid_cutoff',
    'processorY',
    'timer_report_threshold',
    'user-basis',
    'user-basis-netcdf',
    'xc.authors',
    'xc.functional',
]
