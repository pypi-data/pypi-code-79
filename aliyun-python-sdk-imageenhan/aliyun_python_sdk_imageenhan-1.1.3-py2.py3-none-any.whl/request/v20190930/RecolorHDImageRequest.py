# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkimageenhan.endpoint import endpoint_data

class RecolorHDImageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imageenhan', '2019-09-30', 'RecolorHDImage','imageenhan')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ColorTemplates(self):
		return self.get_body_params().get('ColorTemplate')

	def set_ColorTemplates(self, ColorTemplates):
		for depth1 in range(len(ColorTemplates)):
			if ColorTemplates[depth1].get('Color') is not None:
				self.add_body_params('ColorTemplate.' + str(depth1 + 1) + '.Color', ColorTemplates[depth1].get('Color'))

	def get_Degree(self):
		return self.get_body_params().get('Degree')

	def set_Degree(self,Degree):
		self.add_body_params('Degree', Degree)

	def get_Url(self):
		return self.get_body_params().get('Url')

	def set_Url(self,Url):
		self.add_body_params('Url', Url)

	def get_Mode(self):
		return self.get_body_params().get('Mode')

	def set_Mode(self,Mode):
		self.add_body_params('Mode', Mode)

	def get_ColorCount(self):
		return self.get_body_params().get('ColorCount')

	def set_ColorCount(self,ColorCount):
		self.add_body_params('ColorCount', ColorCount)

	def get_RefUrl(self):
		return self.get_body_params().get('RefUrl')

	def set_RefUrl(self,RefUrl):
		self.add_body_params('RefUrl', RefUrl)