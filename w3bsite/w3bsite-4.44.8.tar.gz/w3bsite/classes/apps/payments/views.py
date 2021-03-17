#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports.
from w3bsite.classes.config import *
from w3bsite.classes import utils, views
from w3bsite.classes import defaults as _defaults_

# the payments views.
class Views(_defaults_.Defaults):
	def __init__(self, 
		# passed Website.x objects.
		defaults=None,
	):
		# defaults.
		_defaults_.Defaults.__init__(self)
		self.assign(defaults.dict())
		
		# urlpatterns.
		if dev0s.system.env.get("MIGRATIONS", format=bool, default=False):
			self.urls = []
		else:
			self.urls = views.build_urls([
				self.Purchase(defaults=defaults),
				self.Cancel(defaults=defaults),
			])

	# purchase.
	class Purchase(views.View):
		def __init__(self, defaults=None):
			views.View.__init__(self, "payments/", "purchase", website=defaults.website, html=f"w3bsite/classes/apps/payments/html/purchase.html")
			_defaults_.Defaults.__init__(self)
			self.assign(defaults.dict())
		def view(self, request):
			if self._maintenance_: return self.maintenance(request)
			return self.render(request)

	# cancel.
	class Cancel(views.View):
		def __init__(self, defaults=None):
			views.View.__init__(self, "payments/", "cancel", website=defaults.website, html=f"w3bsite/classes/apps/payments/html/cancel.html")
			_defaults_.Defaults.__init__(self)
			self.assign(defaults.dict())
		def view(self, request):
			if self._maintenance_: return self.maintenance(request)
			return self.render(request)
