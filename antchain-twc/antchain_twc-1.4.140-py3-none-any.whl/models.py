# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List


class Config(TeaModel):
    """
    Model for initing client
    """
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        security_token: str = None,
        protocol: str = None,
        read_timeout: int = None,
        connect_timeout: int = None,
        http_proxy: str = None,
        https_proxy: str = None,
        endpoint: str = None,
        no_proxy: str = None,
        max_idle_conns: int = None,
        user_agent: str = None,
        socks_5proxy: str = None,
        socks_5net_work: str = None,
        max_idle_time_millis: int = None,
        keep_alive_duration_millis: int = None,
        max_requests: int = None,
        max_requests_per_host: int = None,
    ):
        # accesskey id
        self.access_key_id = access_key_id
        # accesskey secret
        self.access_key_secret = access_key_secret
        # security token
        self.security_token = security_token
        # http protocol
        self.protocol = protocol
        # read timeout
        self.read_timeout = read_timeout
        # connect timeout
        self.connect_timeout = connect_timeout
        # http proxy
        self.http_proxy = http_proxy
        # https proxy
        self.https_proxy = https_proxy
        # endpoint
        self.endpoint = endpoint
        # proxy white list
        self.no_proxy = no_proxy
        # max idle conns
        self.max_idle_conns = max_idle_conns
        # user agent
        self.user_agent = user_agent
        # socks5 proxy
        self.socks_5proxy = socks_5proxy
        # socks5 network
        self.socks_5net_work = socks_5net_work
        # 长链接最大空闲时长
        self.max_idle_time_millis = max_idle_time_millis
        # 长链接最大连接时长
        self.keep_alive_duration_millis = keep_alive_duration_millis
        # 最大连接数（长链接最大总数）
        self.max_requests = max_requests
        # 每个目标主机的最大连接数（分主机域名的长链接最大总数
        self.max_requests_per_host = max_requests_per_host

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['accessKeySecret'] = self.access_key_secret
        if self.security_token is not None:
            result['securityToken'] = self.security_token
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.read_timeout is not None:
            result['readTimeout'] = self.read_timeout
        if self.connect_timeout is not None:
            result['connectTimeout'] = self.connect_timeout
        if self.http_proxy is not None:
            result['httpProxy'] = self.http_proxy
        if self.https_proxy is not None:
            result['httpsProxy'] = self.https_proxy
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.no_proxy is not None:
            result['noProxy'] = self.no_proxy
        if self.max_idle_conns is not None:
            result['maxIdleConns'] = self.max_idle_conns
        if self.user_agent is not None:
            result['userAgent'] = self.user_agent
        if self.socks_5proxy is not None:
            result['socks5Proxy'] = self.socks_5proxy
        if self.socks_5net_work is not None:
            result['socks5NetWork'] = self.socks_5net_work
        if self.max_idle_time_millis is not None:
            result['maxIdleTimeMillis'] = self.max_idle_time_millis
        if self.keep_alive_duration_millis is not None:
            result['keepAliveDurationMillis'] = self.keep_alive_duration_millis
        if self.max_requests is not None:
            result['maxRequests'] = self.max_requests
        if self.max_requests_per_host is not None:
            result['maxRequestsPerHost'] = self.max_requests_per_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('accessKeySecret') is not None:
            self.access_key_secret = m.get('accessKeySecret')
        if m.get('securityToken') is not None:
            self.security_token = m.get('securityToken')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('readTimeout') is not None:
            self.read_timeout = m.get('readTimeout')
        if m.get('connectTimeout') is not None:
            self.connect_timeout = m.get('connectTimeout')
        if m.get('httpProxy') is not None:
            self.http_proxy = m.get('httpProxy')
        if m.get('httpsProxy') is not None:
            self.https_proxy = m.get('httpsProxy')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('noProxy') is not None:
            self.no_proxy = m.get('noProxy')
        if m.get('maxIdleConns') is not None:
            self.max_idle_conns = m.get('maxIdleConns')
        if m.get('userAgent') is not None:
            self.user_agent = m.get('userAgent')
        if m.get('socks5Proxy') is not None:
            self.socks_5proxy = m.get('socks5Proxy')
        if m.get('socks5NetWork') is not None:
            self.socks_5net_work = m.get('socks5NetWork')
        if m.get('maxIdleTimeMillis') is not None:
            self.max_idle_time_millis = m.get('maxIdleTimeMillis')
        if m.get('keepAliveDurationMillis') is not None:
            self.keep_alive_duration_millis = m.get('keepAliveDurationMillis')
        if m.get('maxRequests') is not None:
            self.max_requests = m.get('maxRequests')
        if m.get('maxRequestsPerHost') is not None:
            self.max_requests_per_host = m.get('maxRequestsPerHost')
        return self


class ContractFlowSigner(TeaModel):
    def __init__(
        self,
        sign_order: int = None,
        sign_status: int = None,
        signer_account_id: str = None,
        signer_name: str = None,
        signer_real_name: bool = None,
        signer_authorized_account_id: str = None,
        signer_authorized_account_name: str = None,
        signer_authorized_account_real_name: bool = None,
        signer_authorized_account_type: int = None,
        third_order_no: str = None,
    ):
        # 签署顺序
        self.sign_order = sign_order
        # 签署状态, 0-待签, 1-未签, 2-已签 3-待审批 4-拒签
        self.sign_status = sign_status
        # 签署人账号id
        self.signer_account_id = signer_account_id
        # 签署人名称
        self.signer_name = signer_name
        # 签署人是否已实名
        self.signer_real_name = signer_real_name
        # 签约主体的账号id（个人/企业）；如签署人本签署，则返回签署人账号id；如签署人代机构签署，则返回机构账号id
        self.signer_authorized_account_id = signer_authorized_account_id
        # 签约主体名称
        self.signer_authorized_account_name = signer_authorized_account_name
        # 签署主体是否已实名
        self.signer_authorized_account_real_name = signer_authorized_account_real_name
        # 签署主体类型, 0-个人, 1-机构
        self.signer_authorized_account_type = signer_authorized_account_type
        # 本次签署任务对应指定的第三方业务流水号id，当存在多个第三方业务流水号id时，返回多个，并逗号隔开
        self.third_order_no = third_order_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sign_order is not None:
            result['sign_order'] = self.sign_order
        if self.sign_status is not None:
            result['sign_status'] = self.sign_status
        if self.signer_account_id is not None:
            result['signer_account_id'] = self.signer_account_id
        if self.signer_name is not None:
            result['signer_name'] = self.signer_name
        if self.signer_real_name is not None:
            result['signer_real_name'] = self.signer_real_name
        if self.signer_authorized_account_id is not None:
            result['signer_authorized_account_id'] = self.signer_authorized_account_id
        if self.signer_authorized_account_name is not None:
            result['signer_authorized_account_name'] = self.signer_authorized_account_name
        if self.signer_authorized_account_real_name is not None:
            result['signer_authorized_account_real_name'] = self.signer_authorized_account_real_name
        if self.signer_authorized_account_type is not None:
            result['signer_authorized_account_type'] = self.signer_authorized_account_type
        if self.third_order_no is not None:
            result['third_order_no'] = self.third_order_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sign_order') is not None:
            self.sign_order = m.get('sign_order')
        if m.get('sign_status') is not None:
            self.sign_status = m.get('sign_status')
        if m.get('signer_account_id') is not None:
            self.signer_account_id = m.get('signer_account_id')
        if m.get('signer_name') is not None:
            self.signer_name = m.get('signer_name')
        if m.get('signer_real_name') is not None:
            self.signer_real_name = m.get('signer_real_name')
        if m.get('signer_authorized_account_id') is not None:
            self.signer_authorized_account_id = m.get('signer_authorized_account_id')
        if m.get('signer_authorized_account_name') is not None:
            self.signer_authorized_account_name = m.get('signer_authorized_account_name')
        if m.get('signer_authorized_account_real_name') is not None:
            self.signer_authorized_account_real_name = m.get('signer_authorized_account_real_name')
        if m.get('signer_authorized_account_type') is not None:
            self.signer_authorized_account_type = m.get('signer_authorized_account_type')
        if m.get('third_order_no') is not None:
            self.third_order_no = m.get('third_order_no')
        return self


class NotaryCheckMeta(TeaModel):
    def __init__(
        self,
        agency_code: str = None,
        hash_algorithm: str = None,
        notary_content: str = None,
        tx_hash: str = None,
        application_code: str = None,
    ):
        # 对应的法院编号
        self.agency_code = agency_code
        # 哈希算法, notary_type 为 HASH 时此参数必填
        self.hash_algorithm = hash_algorithm
        # 存证内容
        self.notary_content = notary_content
        # 交易哈希
        self.tx_hash = tx_hash
        # 应用ID
        self.application_code = application_code

    def validate(self):
        self.validate_required(self.notary_content, 'notary_content')
        self.validate_required(self.tx_hash, 'tx_hash')

    def to_map(self):
        result = dict()
        if self.agency_code is not None:
            result['agency_code'] = self.agency_code
        if self.hash_algorithm is not None:
            result['hash_algorithm'] = self.hash_algorithm
        if self.notary_content is not None:
            result['notary_content'] = self.notary_content
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        if self.application_code is not None:
            result['application_code'] = self.application_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agency_code') is not None:
            self.agency_code = m.get('agency_code')
        if m.get('hash_algorithm') is not None:
            self.hash_algorithm = m.get('hash_algorithm')
        if m.get('notary_content') is not None:
            self.notary_content = m.get('notary_content')
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        if m.get('application_code') is not None:
            self.application_code = m.get('application_code')
        return self


class SupplierProductInfo(TeaModel):
    def __init__(
        self,
        extra_info: str = None,
        product_id: str = None,
        product_imei_id: str = None,
        product_name: str = None,
        product_number: int = None,
        product_price: int = None,
        supplier_version: str = None,
    ):
        # 产品额外信息
        self.extra_info = extra_info
        # 产品id
        self.product_id = product_id
        # 电子商品唯一标识码
        self.product_imei_id = product_imei_id
        # 产品名称
        self.product_name = product_name
        # 采购产品的个数
        self.product_number = product_number
        # 采购产品的价格，精确到毫厘，如12.34元表示为123400
        self.product_price = product_price
        # 产品版本
        self.supplier_version = supplier_version

    def validate(self):
        self.validate_required(self.product_id, 'product_id')
        self.validate_required(self.product_imei_id, 'product_imei_id')
        self.validate_required(self.product_name, 'product_name')
        if self.product_name is not None:
            self.validate_max_length(self.product_name, 'product_name', 50)
        self.validate_required(self.product_number, 'product_number')
        self.validate_required(self.product_price, 'product_price')

    def to_map(self):
        result = dict()
        if self.extra_info is not None:
            result['extra_info'] = self.extra_info
        if self.product_id is not None:
            result['product_id'] = self.product_id
        if self.product_imei_id is not None:
            result['product_imei_id'] = self.product_imei_id
        if self.product_name is not None:
            result['product_name'] = self.product_name
        if self.product_number is not None:
            result['product_number'] = self.product_number
        if self.product_price is not None:
            result['product_price'] = self.product_price
        if self.supplier_version is not None:
            result['supplier_version'] = self.supplier_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extra_info') is not None:
            self.extra_info = m.get('extra_info')
        if m.get('product_id') is not None:
            self.product_id = m.get('product_id')
        if m.get('product_imei_id') is not None:
            self.product_imei_id = m.get('product_imei_id')
        if m.get('product_name') is not None:
            self.product_name = m.get('product_name')
        if m.get('product_number') is not None:
            self.product_number = m.get('product_number')
        if m.get('product_price') is not None:
            self.product_price = m.get('product_price')
        if m.get('supplier_version') is not None:
            self.supplier_version = m.get('supplier_version')
        return self


class Identity(TeaModel):
    def __init__(
        self,
        agent: str = None,
        agent_id: str = None,
        cert_name: str = None,
        cert_no: str = None,
        cert_type: str = None,
        legal_person: str = None,
        legal_person_id: str = None,
        mobile_no: str = None,
        properties: str = None,
        user_type: str = None,
        agent_cert_type: str = None,
        legal_person_cert_type: str = None,
    ):
        # 经办人姓名，企业认证选填
        self.agent = agent
        # 经办人身份证，企业认证选填
        self.agent_id = agent_id
        # 用户名称
        self.cert_name = cert_name
        # 证件号
        self.cert_no = cert_no
        # 证件类型，个人只支持身份证IDENTITY_CARD，企业支持UNIFIED_SOCIAL_CREDIT_CODE（统一社会信用代码）和ENTERPRISE_REGISTERED_NUMBER（企业工商注册号）
        self.cert_type = cert_type
        # 法人姓名，企业认证必选
        self.legal_person = legal_person
        # 法人身份证，企业认证必选
        self.legal_person_id = legal_person_id
        # 用户手机号码
        self.mobile_no = mobile_no
        # 扩展属性
        self.properties = properties
        # 用户类型，PERSON或者ENTERPRISE
        self.user_type = user_type
        # 经办人证件类型，企业认证选填
        self.agent_cert_type = agent_cert_type
        # 法人证件类型，企业认证必选
        self.legal_person_cert_type = legal_person_cert_type

    def validate(self):
        self.validate_required(self.cert_name, 'cert_name')
        self.validate_required(self.cert_no, 'cert_no')
        self.validate_required(self.cert_type, 'cert_type')
        self.validate_required(self.user_type, 'user_type')

    def to_map(self):
        result = dict()
        if self.agent is not None:
            result['agent'] = self.agent
        if self.agent_id is not None:
            result['agent_id'] = self.agent_id
        if self.cert_name is not None:
            result['cert_name'] = self.cert_name
        if self.cert_no is not None:
            result['cert_no'] = self.cert_no
        if self.cert_type is not None:
            result['cert_type'] = self.cert_type
        if self.legal_person is not None:
            result['legal_person'] = self.legal_person
        if self.legal_person_id is not None:
            result['legal_person_id'] = self.legal_person_id
        if self.mobile_no is not None:
            result['mobile_no'] = self.mobile_no
        if self.properties is not None:
            result['properties'] = self.properties
        if self.user_type is not None:
            result['user_type'] = self.user_type
        if self.agent_cert_type is not None:
            result['agent_cert_type'] = self.agent_cert_type
        if self.legal_person_cert_type is not None:
            result['legal_person_cert_type'] = self.legal_person_cert_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent') is not None:
            self.agent = m.get('agent')
        if m.get('agent_id') is not None:
            self.agent_id = m.get('agent_id')
        if m.get('cert_name') is not None:
            self.cert_name = m.get('cert_name')
        if m.get('cert_no') is not None:
            self.cert_no = m.get('cert_no')
        if m.get('cert_type') is not None:
            self.cert_type = m.get('cert_type')
        if m.get('legal_person') is not None:
            self.legal_person = m.get('legal_person')
        if m.get('legal_person_id') is not None:
            self.legal_person_id = m.get('legal_person_id')
        if m.get('mobile_no') is not None:
            self.mobile_no = m.get('mobile_no')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('user_type') is not None:
            self.user_type = m.get('user_type')
        if m.get('agent_cert_type') is not None:
            self.agent_cert_type = m.get('agent_cert_type')
        if m.get('legal_person_cert_type') is not None:
            self.legal_person_cert_type = m.get('legal_person_cert_type')
        return self


class ContractDocAddress(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        file_name: str = None,
        file_url: str = None,
        tx_hash: str = None,
    ):
        # 电子合同文档ID
        self.file_id = file_id
        # 电子合同文档名称，默认文件名称
        self.file_name = file_name
        # 电子合同下载文档地址, 有效时间1小时
        self.file_url = file_url
        # 合同文件的存证地址
        self.tx_hash = tx_hash

    def validate(self):
        self.validate_required(self.file_id, 'file_id')
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.file_url, 'file_url')

    def to_map(self):
        result = dict()
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.file_name is not None:
            result['file_name'] = self.file_name
        if self.file_url is not None:
            result['file_url'] = self.file_url
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        if m.get('file_url') is not None:
            self.file_url = m.get('file_url')
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class LeaseOrderExtra(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 额外信息的主键
        self.key = key
        # 额外信息的值
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ContractPlatformSignField(TeaModel):
    def __init__(
        self,
        add_sign_time: bool = None,
        order: int = None,
        pos_page: str = None,
        pos_x: str = None,
        pos_y: str = None,
        seal_id: str = None,
        third_order_no: str = None,
        width: str = None,
    ):
        # 是否添加签署时间戳，默认不添加，时间格式如"2019-03-11 10:12:12"
        self.add_sign_time = add_sign_time
        # 签署区顺序，默认1,且不小于1，顺序越小越先处理
        self.order = order
        # 页码信息，当签署区signType为2时, 页码可以'-'分割, 其他情况只能是数字
        self.pos_page = pos_page
        # x坐标转为字符串的值，默认空
        self.pos_x = pos_x
        # y坐标转为字符串的值
        self.pos_y = pos_y
        # 印章id ，如不传，则采用账号下的默认印章
        self.seal_id = seal_id
        # 第三方业务流水号id，保证相同签署人、相同签约主体、相同签署顺序的任务，对应的第三方业务流水id唯一，默认空
        self.third_order_no = third_order_no
        # 签署区宽，默认印章宽度
        self.width = width

    def validate(self):
        self.validate_required(self.pos_page, 'pos_page')
        self.validate_required(self.pos_y, 'pos_y')

    def to_map(self):
        result = dict()
        if self.add_sign_time is not None:
            result['add_sign_time'] = self.add_sign_time
        if self.order is not None:
            result['order'] = self.order
        if self.pos_page is not None:
            result['pos_page'] = self.pos_page
        if self.pos_x is not None:
            result['pos_x'] = self.pos_x
        if self.pos_y is not None:
            result['pos_y'] = self.pos_y
        if self.seal_id is not None:
            result['seal_id'] = self.seal_id
        if self.third_order_no is not None:
            result['third_order_no'] = self.third_order_no
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('add_sign_time') is not None:
            self.add_sign_time = m.get('add_sign_time')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('pos_page') is not None:
            self.pos_page = m.get('pos_page')
        if m.get('pos_x') is not None:
            self.pos_x = m.get('pos_x')
        if m.get('pos_y') is not None:
            self.pos_y = m.get('pos_y')
        if m.get('seal_id') is not None:
            self.seal_id = m.get('seal_id')
        if m.get('third_order_no') is not None:
            self.third_order_no = m.get('third_order_no')
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class NotaryCheckResult(TeaModel):
    def __init__(
        self,
        block_height: int = None,
        error_code: int = None,
        error_message: str = None,
        notary_time: str = None,
        notary_type: str = None,
        result: bool = None,
        transaction_id: str = None,
        tx_hash: str = None,
        block_hash: str = None,
        phase: str = None,
    ):
        # 存证所在区块高度
        self.block_height = block_height
        # 核验结果错误码
        self.error_code = error_code
        # 错误信息
        self.error_message = error_message
        # 存证时间
        self.notary_time = notary_time
        # 存证类型
        self.notary_type = notary_type
        # 核验是否成功
        self.result = result
        # 存证事务ID
        self.transaction_id = transaction_id
        # 交易哈希
        self.tx_hash = tx_hash
        # 区块哈希
        self.block_hash = block_hash
        # 存证阶段
        self.phase = phase

    def validate(self):
        self.validate_required(self.block_height, 'block_height')
        if self.block_height is not None:
            self.validate_minimum(self.block_height, 'block_height', 0)
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.notary_time, 'notary_time')
        if self.notary_time is not None:
            self.validate_pattern(self.notary_time, 'notary_time', '\\d{4}[-]\\d{1,2}[-]\\d{1,2}[T]\\d{2}:\\d{2}:\\d{2}([Z]|([\\.]\\d{1,9})?[\\+]\\d{2}[\\:]?\\d{2})')
        self.validate_required(self.notary_type, 'notary_type')
        self.validate_required(self.result, 'result')
        self.validate_required(self.transaction_id, 'transaction_id')
        self.validate_required(self.tx_hash, 'tx_hash')
        self.validate_required(self.block_hash, 'block_hash')
        self.validate_required(self.phase, 'phase')

    def to_map(self):
        result = dict()
        if self.block_height is not None:
            result['block_height'] = self.block_height
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_message is not None:
            result['error_message'] = self.error_message
        if self.notary_time is not None:
            result['notary_time'] = self.notary_time
        if self.notary_type is not None:
            result['notary_type'] = self.notary_type
        if self.result is not None:
            result['result'] = self.result
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        if self.block_hash is not None:
            result['block_hash'] = self.block_hash
        if self.phase is not None:
            result['phase'] = self.phase
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('block_height') is not None:
            self.block_height = m.get('block_height')
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_message') is not None:
            self.error_message = m.get('error_message')
        if m.get('notary_time') is not None:
            self.notary_time = m.get('notary_time')
        if m.get('notary_type') is not None:
            self.notary_type = m.get('notary_type')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        if m.get('block_hash') is not None:
            self.block_hash = m.get('block_hash')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        return self


class ContractNotaryDocumentInfo(TeaModel):
    def __init__(
        self,
        content: str = None,
        signatories: str = None,
        timestamp: str = None,
        tx_hash: str = None,
        file_id: str = None,
    ):
        # 签署完成的合同hash
        self.content = content
        # 签署人ID（支持多个，不同ID间用“,”分隔开）
        self.signatories = signatories
        # 存证结束时间，UNIX时间戳(毫秒)
        self.timestamp = timestamp
        # 存证凭据，仅在批量核验时需要填写
        self.tx_hash = tx_hash
        # 签署的文件ID
        self.file_id = file_id

    def validate(self):
        self.validate_required(self.content, 'content')
        self.validate_required(self.signatories, 'signatories')
        self.validate_required(self.timestamp, 'timestamp')
        self.validate_required(self.file_id, 'file_id')

    def to_map(self):
        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.signatories is not None:
            result['signatories'] = self.signatories
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('signatories') is not None:
            self.signatories = m.get('signatories')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class ContractSignField(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        file_id: str = None,
        signfield_id: str = None,
    ):
        # 电子合同用户ID
        self.account_id = account_id
        # 电子合同文档ID
        self.file_id = file_id
        # 电子合同签署区id
        self.signfield_id = signfield_id

    def validate(self):
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.file_id, 'file_id')
        self.validate_required(self.signfield_id, 'signfield_id')

    def to_map(self):
        result = dict()
        if self.account_id is not None:
            result['account_id'] = self.account_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.signfield_id is not None:
            result['signfield_id'] = self.signfield_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('account_id') is not None:
            self.account_id = m.get('account_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('signfield_id') is not None:
            self.signfield_id = m.get('signfield_id')
        return self


class ContractAccount(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ContractNotarySignInfo(TeaModel):
    def __init__(
        self,
        content: str = None,
        contract_hash: str = None,
        signatory: str = None,
        timestamp: str = None,
        tx_hash: str = None,
    ):
        # 本阶段存证内容哈希值
        self.content = content
        # 电子合同文件hash，可能一次性签署多个文件，不同文件的hash间用“,”分隔开
        self.contract_hash = contract_hash
        # 签署人ID
        self.signatory = signatory
        # 存证阶段发生时间，UNIX时间戳(毫秒)
        self.timestamp = timestamp
        # 存证凭据，仅在批量核验时需要填写
        self.tx_hash = tx_hash

    def validate(self):
        self.validate_required(self.content, 'content')
        self.validate_required(self.contract_hash, 'contract_hash')
        self.validate_required(self.signatory, 'signatory')
        self.validate_required(self.timestamp, 'timestamp')

    def to_map(self):
        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.contract_hash is not None:
            result['contract_hash'] = self.contract_hash
        if self.signatory is not None:
            result['signatory'] = self.signatory
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('contract_hash') is not None:
            self.contract_hash = m.get('contract_hash')
        if m.get('signatory') is not None:
            self.signatory = m.get('signatory')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class WitnessConfirmData(TeaModel):
    def __init__(
        self,
        doc_file_key: str = None,
        hash_algorithm: str = None,
        signed_hash: str = None,
        third_doc_id: str = None,
    ):
        # 文档fileKey
        self.doc_file_key = doc_file_key
        # 文档摘要算法，SHA256
        self.hash_algorithm = hash_algorithm
        # 签署后文档摘要值
        self.signed_hash = signed_hash
        # 第三方文档id
        self.third_doc_id = third_doc_id

    def validate(self):
        self.validate_required(self.hash_algorithm, 'hash_algorithm')
        self.validate_required(self.signed_hash, 'signed_hash')
        self.validate_required(self.third_doc_id, 'third_doc_id')

    def to_map(self):
        result = dict()
        if self.doc_file_key is not None:
            result['doc_file_key'] = self.doc_file_key
        if self.hash_algorithm is not None:
            result['hash_algorithm'] = self.hash_algorithm
        if self.signed_hash is not None:
            result['signed_hash'] = self.signed_hash
        if self.third_doc_id is not None:
            result['third_doc_id'] = self.third_doc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('doc_file_key') is not None:
            self.doc_file_key = m.get('doc_file_key')
        if m.get('hash_algorithm') is not None:
            self.hash_algorithm = m.get('hash_algorithm')
        if m.get('signed_hash') is not None:
            self.signed_hash = m.get('signed_hash')
        if m.get('third_doc_id') is not None:
            self.third_doc_id = m.get('third_doc_id')
        return self


class ContractOrganizationApplication(TeaModel):
    def __init__(
        self,
        id_number: str = None,
        id_type: str = None,
        legal_person: str = None,
        legal_person_id: str = None,
        name: str = None,
        organization_id: str = None,
    ):
        # 证件号
        self.id_number = id_number
        # 证件类型，默认CRED_ORG_USCC，详见机构证件类型说明 （https://tech.antfin.com/docs/2/155166）
        self.id_type = id_type
        # 企业法人名称
        self.legal_person = legal_person
        # 企业法人证件号
        self.legal_person_id = legal_person_id
        # 机构名称
        self.name = name
        # 机构唯一标识，可传入第三方平台的机构用户id等
        self.organization_id = organization_id

    def validate(self):
        self.validate_required(self.id_number, 'id_number')
        self.validate_required(self.id_type, 'id_type')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = dict()
        if self.id_number is not None:
            result['id_number'] = self.id_number
        if self.id_type is not None:
            result['id_type'] = self.id_type
        if self.legal_person is not None:
            result['legal_person'] = self.legal_person
        if self.legal_person_id is not None:
            result['legal_person_id'] = self.legal_person_id
        if self.name is not None:
            result['name'] = self.name
        if self.organization_id is not None:
            result['organization_id'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id_number') is not None:
            self.id_number = m.get('id_number')
        if m.get('id_type') is not None:
            self.id_type = m.get('id_type')
        if m.get('legal_person') is not None:
            self.legal_person = m.get('legal_person')
        if m.get('legal_person_id') is not None:
            self.legal_person_id = m.get('legal_person_id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('organization_id') is not None:
            self.organization_id = m.get('organization_id')
        return self


class Location(TeaModel):
    def __init__(
        self,
        city: str = None,
        imei: str = None,
        imsi: str = None,
        ip: str = None,
        latitude: str = None,
        longitude: str = None,
        mac_addr: str = None,
        properties: str = None,
    ):
        # 所在城市
        self.city = city
        # 使用设备的IMEI号
        self.imei = imei
        # 使用设备的IMSI号
        self.imsi = imsi
        # 使用设备的IP地址
        self.ip = ip
        # 纬度
        self.latitude = latitude
        # 经度
        self.longitude = longitude
        # 使用设备的Wi-Fi物理地址
        self.mac_addr = mac_addr
        # 扩展属性
        self.properties = properties

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.city is not None:
            result['city'] = self.city
        if self.imei is not None:
            result['imei'] = self.imei
        if self.imsi is not None:
            result['imsi'] = self.imsi
        if self.ip is not None:
            result['ip'] = self.ip
        if self.latitude is not None:
            result['latitude'] = self.latitude
        if self.longitude is not None:
            result['longitude'] = self.longitude
        if self.mac_addr is not None:
            result['mac_addr'] = self.mac_addr
        if self.properties is not None:
            result['properties'] = self.properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('imei') is not None:
            self.imei = m.get('imei')
        if m.get('imsi') is not None:
            self.imsi = m.get('imsi')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')
        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')
        if m.get('mac_addr') is not None:
            self.mac_addr = m.get('mac_addr')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        return self


class ContractNotaryFinishInfo(TeaModel):
    def __init__(
        self,
        content: str = None,
        file_num: int = None,
        initiator: str = None,
        signatories: str = None,
        timestamp: str = None,
        tx_hash: str = None,
        user_types: str = None,
        business_type: str = None,
        amounts: str = None,
    ):
        # 本阶段存证内容哈希值
        self.content = content
        # 签署文件份数
        self.file_num = file_num
        # 发起人ID
        self.initiator = initiator
        # 签署人ID（支持多个，不同ID间用“,”分隔开）
        self.signatories = signatories
        # 存证阶段发生时间，UNIX时间戳(毫秒)
        self.timestamp = timestamp
        # 存证凭据，仅在批量核验时需要填写
        self.tx_hash = tx_hash
        # signatories对应的用户类型
        self.user_types = user_types
        # 签署合同所属行业
        self.business_type = business_type
        # 合同对应的金额，如果不涉及金额，填充为0，个数与file_num对应
        self.amounts = amounts

    def validate(self):
        self.validate_required(self.content, 'content')
        self.validate_required(self.file_num, 'file_num')
        self.validate_required(self.initiator, 'initiator')
        self.validate_required(self.signatories, 'signatories')
        self.validate_required(self.timestamp, 'timestamp')

    def to_map(self):
        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.file_num is not None:
            result['file_num'] = self.file_num
        if self.initiator is not None:
            result['initiator'] = self.initiator
        if self.signatories is not None:
            result['signatories'] = self.signatories
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        if self.user_types is not None:
            result['user_types'] = self.user_types
        if self.business_type is not None:
            result['business_type'] = self.business_type
        if self.amounts is not None:
            result['amounts'] = self.amounts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('file_num') is not None:
            self.file_num = m.get('file_num')
        if m.get('initiator') is not None:
            self.initiator = m.get('initiator')
        if m.get('signatories') is not None:
            self.signatories = m.get('signatories')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        if m.get('user_types') is not None:
            self.user_types = m.get('user_types')
        if m.get('business_type') is not None:
            self.business_type = m.get('business_type')
        if m.get('amounts') is not None:
            self.amounts = m.get('amounts')
        return self


class ContractNotaryInfo(TeaModel):
    def __init__(
        self,
        tx_hash: str = None,
        doc_id: str = None,
        content_hash: str = None,
        transaction_id: str = None,
    ):
        # 存证地址
        self.tx_hash = tx_hash
        # 存证相关联的文档ID
        self.doc_id = doc_id
        # 存证的内容哈希值
        self.content_hash = content_hash
        # 存证事务ID
        self.transaction_id = transaction_id

    def validate(self):
        self.validate_required(self.tx_hash, 'tx_hash')
        self.validate_required(self.transaction_id, 'transaction_id')

    def to_map(self):
        result = dict()
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        if self.doc_id is not None:
            result['doc_id'] = self.doc_id
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        if m.get('doc_id') is not None:
            self.doc_id = m.get('doc_id')
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        return self


class ContractSignFieldApplication(TeaModel):
    def __init__(
        self,
        add_sign_time: bool = None,
        authorized_account_id: str = None,
        file_id: str = None,
        order: int = None,
        pos_page: str = None,
        pos_x: str = None,
        pos_y: str = None,
        seal_id: str = None,
        third_order_no: str = None,
        width: str = None,
        sign_type: int = None,
    ):
        # 是否添加签署时间戳，默认不添加，时间格式如"2019-03-11 10:12:12"
        self.add_sign_time = add_sign_time
        # 签约主体账号标识， 将使用该主体账号对应的数字证书完成本次签署，如：当存在签署操作人代某机构签署时，需要传入该机构的账号id
        self.authorized_account_id = authorized_account_id
        # 电子合同文件ID
        self.file_id = file_id
        # 签署区顺序，默认1,且不小于1，顺序越小越先处理
        self.order = order
        # 页码信息
        self.pos_page = pos_page
        # x坐标转为字符串的值，默认空，页面签章必填，骑缝签章不填写
        self.pos_x = pos_x
        # y坐标转为字符串的值
        self.pos_y = pos_y
        # 印章id ，如不传，则采用账号下的默认印章
        self.seal_id = seal_id
        # 第三方业务流水号id，保证相同签署人、相同签约主体、相同签署顺序的任务，对应的第三方业务流水id唯一，默认空
        self.third_order_no = third_order_no
        # 签署区宽，默认印章宽度
        self.width = width
        # 签署类型，0-不限，1-单页签署，2-骑缝签署，默认1
        self.sign_type = sign_type

    def validate(self):
        self.validate_required(self.authorized_account_id, 'authorized_account_id')
        self.validate_required(self.file_id, 'file_id')
        self.validate_required(self.pos_y, 'pos_y')

    def to_map(self):
        result = dict()
        if self.add_sign_time is not None:
            result['add_sign_time'] = self.add_sign_time
        if self.authorized_account_id is not None:
            result['authorized_account_id'] = self.authorized_account_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.order is not None:
            result['order'] = self.order
        if self.pos_page is not None:
            result['pos_page'] = self.pos_page
        if self.pos_x is not None:
            result['pos_x'] = self.pos_x
        if self.pos_y is not None:
            result['pos_y'] = self.pos_y
        if self.seal_id is not None:
            result['seal_id'] = self.seal_id
        if self.third_order_no is not None:
            result['third_order_no'] = self.third_order_no
        if self.width is not None:
            result['width'] = self.width
        if self.sign_type is not None:
            result['sign_type'] = self.sign_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('add_sign_time') is not None:
            self.add_sign_time = m.get('add_sign_time')
        if m.get('authorized_account_id') is not None:
            self.authorized_account_id = m.get('authorized_account_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('pos_page') is not None:
            self.pos_page = m.get('pos_page')
        if m.get('pos_x') is not None:
            self.pos_x = m.get('pos_x')
        if m.get('pos_y') is not None:
            self.pos_y = m.get('pos_y')
        if m.get('seal_id') is not None:
            self.seal_id = m.get('seal_id')
        if m.get('third_order_no') is not None:
            self.third_order_no = m.get('third_order_no')
        if m.get('width') is not None:
            self.width = m.get('width')
        if m.get('sign_type') is not None:
            self.sign_type = m.get('sign_type')
        return self


class ContractHandSignFieldApplication(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        file_id: str = None,
        order: int = None,
        pos_page: str = None,
        pos_x: str = None,
        pos_y: str = None,
        seal_id: str = None,
        sign_date_bean_type: int = None,
        sign_date_font_size: int = None,
        sign_date_format: str = None,
        sign_date_pos_page: int = None,
        sign_date_pos_x: str = None,
        sign_date_pos_y: str = None,
        sign_type: int = None,
        third_order_no: str = None,
        width: str = None,
        seal_ids: List[str] = None,
    ):
        # 签署操作人个人账号标识，即操作本次签署的个人，如需通知用户签署，则系统向该账号下绑定的手机、邮箱发送签署链接
        self.account_id = account_id
        # 电子合同文件ID
        self.file_id = file_id
        # 签署区顺序，默认1,且不小于1，顺序越小越先处理
        self.order = order
        # 页码信息，当签署区signType为2时, 页码可以'-'分割, 其他情况只能是数字
        self.pos_page = pos_page
        # x坐标，页面签章必填，骑缝签章不填写
        self.pos_x = pos_x
        # y坐标
        self.pos_y = pos_y
        # 印章id
        self.seal_id = seal_id
        # 是否需要添加签署日期，0-禁止 1-必须 2-不限制，默认0
        self.sign_date_bean_type = sign_date_bean_type
        # 签章日期字体大小,默认12
        self.sign_date_font_size = sign_date_font_size
        # 签章日期格式，yyyy年MM月dd日
        self.sign_date_format = sign_date_format
        # 页码信息，当signDateBeanType为1时，代表签署的印章必须展示签署日期，默认放在印章正下方，签署人可拖拽日期到当前页面的其他位置，如果发起方指定签署位置的同时，需要同时指定日期盖章位置，则需传入日期盖章页码（与印章页码相同），在传入X\Y坐标即可。
        self.sign_date_pos_page = sign_date_pos_page
        # 签章日期x坐标，默认0
        self.sign_date_pos_x = sign_date_pos_x
        # 签章日期y坐标，默认0
        self.sign_date_pos_y = sign_date_pos_y
        # 签署类型，0-不限，1-单页签署，2-骑缝签署，默认1
        self.sign_type = sign_type
        # 第三方业务流水号id，保证相同签署人、相同签约主体、相同签署顺序的任务，对应的第三方业务流水id唯一，默认空
        self.third_order_no = third_order_no
        # 签署区宽，默认印章宽度
        self.width = width
        # 印章ids，只支持企业用户进行印章ID列表的设置；用于手动签署时，指定企业印章进行展示，实现手动选择印章进行签署。
        self.seal_ids = seal_ids

    def validate(self):
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.file_id, 'file_id')
        self.validate_required(self.pos_page, 'pos_page')
        self.validate_required(self.pos_y, 'pos_y')

    def to_map(self):
        result = dict()
        if self.account_id is not None:
            result['account_id'] = self.account_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.order is not None:
            result['order'] = self.order
        if self.pos_page is not None:
            result['pos_page'] = self.pos_page
        if self.pos_x is not None:
            result['pos_x'] = self.pos_x
        if self.pos_y is not None:
            result['pos_y'] = self.pos_y
        if self.seal_id is not None:
            result['seal_id'] = self.seal_id
        if self.sign_date_bean_type is not None:
            result['sign_date_bean_type'] = self.sign_date_bean_type
        if self.sign_date_font_size is not None:
            result['sign_date_font_size'] = self.sign_date_font_size
        if self.sign_date_format is not None:
            result['sign_date_format'] = self.sign_date_format
        if self.sign_date_pos_page is not None:
            result['sign_date_pos_page'] = self.sign_date_pos_page
        if self.sign_date_pos_x is not None:
            result['sign_date_pos_x'] = self.sign_date_pos_x
        if self.sign_date_pos_y is not None:
            result['sign_date_pos_y'] = self.sign_date_pos_y
        if self.sign_type is not None:
            result['sign_type'] = self.sign_type
        if self.third_order_no is not None:
            result['third_order_no'] = self.third_order_no
        if self.width is not None:
            result['width'] = self.width
        if self.seal_ids is not None:
            result['seal_ids'] = self.seal_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('account_id') is not None:
            self.account_id = m.get('account_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('pos_page') is not None:
            self.pos_page = m.get('pos_page')
        if m.get('pos_x') is not None:
            self.pos_x = m.get('pos_x')
        if m.get('pos_y') is not None:
            self.pos_y = m.get('pos_y')
        if m.get('seal_id') is not None:
            self.seal_id = m.get('seal_id')
        if m.get('sign_date_bean_type') is not None:
            self.sign_date_bean_type = m.get('sign_date_bean_type')
        if m.get('sign_date_font_size') is not None:
            self.sign_date_font_size = m.get('sign_date_font_size')
        if m.get('sign_date_format') is not None:
            self.sign_date_format = m.get('sign_date_format')
        if m.get('sign_date_pos_page') is not None:
            self.sign_date_pos_page = m.get('sign_date_pos_page')
        if m.get('sign_date_pos_x') is not None:
            self.sign_date_pos_x = m.get('sign_date_pos_x')
        if m.get('sign_date_pos_y') is not None:
            self.sign_date_pos_y = m.get('sign_date_pos_y')
        if m.get('sign_type') is not None:
            self.sign_type = m.get('sign_type')
        if m.get('third_order_no') is not None:
            self.third_order_no = m.get('third_order_no')
        if m.get('width') is not None:
            self.width = m.get('width')
        if m.get('seal_ids') is not None:
            self.seal_ids = m.get('seal_ids')
        return self


class WitnessApprovalData(TeaModel):
    def __init__(
        self,
        approval_flow_id: str = None,
        seal_ids: List[str] = None,
    ):
        # 审批流程id
        self.approval_flow_id = approval_flow_id
        # 印章id列表
        self.seal_ids = seal_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.approval_flow_id is not None:
            result['approval_flow_id'] = self.approval_flow_id
        if self.seal_ids is not None:
            result['seal_ids'] = self.seal_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('approval_flow_id') is not None:
            self.approval_flow_id = m.get('approval_flow_id')
        if m.get('seal_ids') is not None:
            self.seal_ids = m.get('seal_ids')
        return self


class RentInfo(TeaModel):
    def __init__(
        self,
        rent_price: int = None,
        rent_term: int = None,
        commission: int = None,
        buyout_price: int = None,
        retained_price: int = None,
    ):
        # 租金
        self.rent_price = rent_price
        # 租期
        self.rent_term = rent_term
        # 手续费
        self.commission = commission
        # 买断价
        self.buyout_price = buyout_price
        # 留购价
        self.retained_price = retained_price

    def validate(self):
        self.validate_required(self.rent_price, 'rent_price')
        self.validate_required(self.rent_term, 'rent_term')
        self.validate_required(self.commission, 'commission')
        self.validate_required(self.buyout_price, 'buyout_price')
        self.validate_required(self.retained_price, 'retained_price')

    def to_map(self):
        result = dict()
        if self.rent_price is not None:
            result['rent_price'] = self.rent_price
        if self.rent_term is not None:
            result['rent_term'] = self.rent_term
        if self.commission is not None:
            result['commission'] = self.commission
        if self.buyout_price is not None:
            result['buyout_price'] = self.buyout_price
        if self.retained_price is not None:
            result['retained_price'] = self.retained_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rent_price') is not None:
            self.rent_price = m.get('rent_price')
        if m.get('rent_term') is not None:
            self.rent_term = m.get('rent_term')
        if m.get('commission') is not None:
            self.commission = m.get('commission')
        if m.get('buyout_price') is not None:
            self.buyout_price = m.get('buyout_price')
        if m.get('retained_price') is not None:
            self.retained_price = m.get('retained_price')
        return self


class NotaryInfo(TeaModel):
    def __init__(
        self,
        content_hash: str = None,
        cooperation: str = None,
        creation_type: str = None,
        file_name: str = None,
        hash_algorithm: str = None,
        platform: str = None,
        size: int = None,
        tx_hash: str = None,
        transaction_id: str = None,
    ):
        # 存证内容的哈希值，默认采用SHA256算法
        self.content_hash = content_hash
        # 合作人（版权存证函专用），会展示在存证证明中
        self.cooperation = cooperation
        # 作品名称类型（版权存证函使用），会展示在存证证明中
        self.creation_type = creation_type
        # 如果是文件存证，可填写文件名称
        self.file_name = file_name
        # 计算content_hash的哈希算法，目前只支持SHA256
        self.hash_algorithm = hash_algorithm
        # 申请平台名，用于在存证函上显示用名称
        self.platform = platform
        # 文件容量，默认为0
        self.size = size
        # 发起存证成功后，返回的存证凭据
        self.tx_hash = tx_hash
        # 存证事务ID
        self.transaction_id = transaction_id

    def validate(self):
        self.validate_required(self.content_hash, 'content_hash')
        self.validate_required(self.tx_hash, 'tx_hash')
        self.validate_required(self.transaction_id, 'transaction_id')

    def to_map(self):
        result = dict()
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.cooperation is not None:
            result['cooperation'] = self.cooperation
        if self.creation_type is not None:
            result['creation_type'] = self.creation_type
        if self.file_name is not None:
            result['file_name'] = self.file_name
        if self.hash_algorithm is not None:
            result['hash_algorithm'] = self.hash_algorithm
        if self.platform is not None:
            result['platform'] = self.platform
        if self.size is not None:
            result['size'] = self.size
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('cooperation') is not None:
            self.cooperation = m.get('cooperation')
        if m.get('creation_type') is not None:
            self.creation_type = m.get('creation_type')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        if m.get('hash_algorithm') is not None:
            self.hash_algorithm = m.get('hash_algorithm')
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        return self


class ProductInfo(TeaModel):
    def __init__(
        self,
        need_did: bool = None,
        product_brand: str = None,
        product_id: str = None,
        product_imei_id: str = None,
        product_model: str = None,
        product_name: str = None,
        product_number: int = None,
        product_price: int = None,
        supplier_id: str = None,
        supplier_version: str = None,
        extra_info: str = None,
    ):
        # 是否需要创建did
        self.need_did = need_did
        # 产品品牌，长度不超过50
        self.product_brand = product_brand
        # 产品Id，长度不超过50
        self.product_id = product_id
        # 唯一标识码，imeiID，长度不超过50
        self.product_imei_id = product_imei_id
        # 产品规格型号，长度不超过255
        self.product_model = product_model
        # 产品名称，长度不超过50
        self.product_name = product_name
        # 产品数量
        self.product_number = product_number
        # 产品采购含税价 精确到毫厘，即123400表示12.34元
        self.product_price = product_price
        # 供应商id
        self.supplier_id = supplier_id
        # 供应商对应的产品版本，每个版本可以对应一个价格
        self.supplier_version = supplier_version
        # 额外字段
        self.extra_info = extra_info

    def validate(self):
        self.validate_required(self.product_id, 'product_id')
        self.validate_required(self.product_name, 'product_name')
        self.validate_required(self.product_number, 'product_number')
        self.validate_required(self.product_price, 'product_price')

    def to_map(self):
        result = dict()
        if self.need_did is not None:
            result['need_did'] = self.need_did
        if self.product_brand is not None:
            result['product_brand'] = self.product_brand
        if self.product_id is not None:
            result['product_id'] = self.product_id
        if self.product_imei_id is not None:
            result['product_imei_id'] = self.product_imei_id
        if self.product_model is not None:
            result['product_model'] = self.product_model
        if self.product_name is not None:
            result['product_name'] = self.product_name
        if self.product_number is not None:
            result['product_number'] = self.product_number
        if self.product_price is not None:
            result['product_price'] = self.product_price
        if self.supplier_id is not None:
            result['supplier_id'] = self.supplier_id
        if self.supplier_version is not None:
            result['supplier_version'] = self.supplier_version
        if self.extra_info is not None:
            result['extra_info'] = self.extra_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('need_did') is not None:
            self.need_did = m.get('need_did')
        if m.get('product_brand') is not None:
            self.product_brand = m.get('product_brand')
        if m.get('product_id') is not None:
            self.product_id = m.get('product_id')
        if m.get('product_imei_id') is not None:
            self.product_imei_id = m.get('product_imei_id')
        if m.get('product_model') is not None:
            self.product_model = m.get('product_model')
        if m.get('product_name') is not None:
            self.product_name = m.get('product_name')
        if m.get('product_number') is not None:
            self.product_number = m.get('product_number')
        if m.get('product_price') is not None:
            self.product_price = m.get('product_price')
        if m.get('supplier_id') is not None:
            self.supplier_id = m.get('supplier_id')
        if m.get('supplier_version') is not None:
            self.supplier_version = m.get('supplier_version')
        if m.get('extra_info') is not None:
            self.extra_info = m.get('extra_info')
        return self


class ContractDoc(TeaModel):
    def __init__(
        self,
        encryption: int = None,
        file_id: str = None,
        file_name: str = None,
        file_password: str = None,
    ):
        # 是否加密，0-不加密，1-加，默认0
        self.encryption = encryption
        # 电子合同文档的ID
        self.file_id = file_id
        # 电子合同文档名称，默认文件名称
        self.file_name = file_name
        # 电子合同文档密码, 如果encryption值为1, 文档密码不能为空，默认没有密码
        self.file_password = file_password

    def validate(self):
        self.validate_required(self.file_id, 'file_id')

    def to_map(self):
        result = dict()
        if self.encryption is not None:
            result['encryption'] = self.encryption
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.file_name is not None:
            result['file_name'] = self.file_name
        if self.file_password is not None:
            result['file_password'] = self.file_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('encryption') is not None:
            self.encryption = m.get('encryption')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        if m.get('file_password') is not None:
            self.file_password = m.get('file_password')
        return self


class LeaseNotaryRecord(TeaModel):
    def __init__(
        self,
        phase: str = None,
        tx_hash: str = None,
    ):
        # 存证阶段
        self.phase = phase
        # 交易哈希，存证记录唯一标识
        self.tx_hash = tx_hash

    def validate(self):
        self.validate_required(self.phase, 'phase')
        self.validate_required(self.tx_hash, 'tx_hash')

    def to_map(self):
        result = dict()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class ContractSignFieldDetail(TeaModel):
    def __init__(
        self,
        actor_indentity_type: int = None,
        add_time: int = None,
        assigned_posbean: bool = None,
        assigned_seal: bool = None,
        authorized_account_id: str = None,
        auto_execute: bool = None,
        execute_failed_reason: str = None,
        file_id: str = None,
        flow_id: str = None,
        order: int = None,
        pos_page: str = None,
        pos_x: str = None,
        pos_y: str = None,
        seal_file_key: str = None,
        seal_id: str = None,
        seal_type: str = None,
        signer_account_id: str = None,
        signfield_id: str = None,
        sign_type: int = None,
        status: int = None,
        status_description: str = None,
        width: str = None,
    ):
        # 签约主体类别，0-个人，1-机构，默认0,2 是不限
        self.actor_indentity_type = actor_indentity_type
        # 添加时间
        self.add_time = add_time
        # 是否指定位置，TRUE表示不允许更新位置，配置项，无默认值
        self.assigned_posbean = assigned_posbean
        # 是否指定印章数据，TRUE表示不允许更新印章，配置项，无默认值
        self.assigned_seal = assigned_seal
        # 签约主体账号标识，将使用该主体账号对应的数字证书完成本次签署，如：当存在签署操作人代某机构签署时，需要传入该机构的账号id
        self.authorized_account_id = authorized_account_id
        # 是否自动执行，TRUE需要静默授权，配置项，无默认值
        self.auto_execute = auto_execute
        # 执行失败原因
        self.execute_failed_reason = execute_failed_reason
        # 文件file id
        self.file_id = file_id
        # 流程id
        self.flow_id = flow_id
        # 签署区顺序，默认1,且不小于1，顺序越小越先处理
        self.order = order
        # 页码信息，可以','或'-'分割
        self.pos_page = pos_page
        # x坐标
        self.pos_x = pos_x
        # y坐标
        self.pos_y = pos_y
        # 印章文件file key
        self.seal_file_key = seal_file_key
        # 印章id
        self.seal_id = seal_id
        # 印章类型，支持多种类型时逗号分割，0-手绘印章，1-模版印章，为空不限制
        self.seal_type = seal_type
        # 签署操作人个人账号标识，即操作本次签署的个人，如需e签宝通知用户签署，则系统向该账号下绑定的手机、邮箱发送签署链接
        self.signer_account_id = signer_account_id
        # 签署区Id
        self.signfield_id = signfield_id
        # 签署类型，0-不限，1-单页签署，2-骑缝签署,4-关键字签署，默认1
        self.sign_type = sign_type
        # 签署区状态（0："等待执行，1："执行中"，2："执行失败"，3："审批中"，4： "执行完成"）
        self.status = status
        # 状态描述
        self.status_description = status_description
        # 签署区宽
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.actor_indentity_type is not None:
            result['actor_indentity_type'] = self.actor_indentity_type
        if self.add_time is not None:
            result['add_time'] = self.add_time
        if self.assigned_posbean is not None:
            result['assigned_posbean'] = self.assigned_posbean
        if self.assigned_seal is not None:
            result['assigned_seal'] = self.assigned_seal
        if self.authorized_account_id is not None:
            result['authorized_account_id'] = self.authorized_account_id
        if self.auto_execute is not None:
            result['auto_execute'] = self.auto_execute
        if self.execute_failed_reason is not None:
            result['execute_failed_reason'] = self.execute_failed_reason
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.order is not None:
            result['order'] = self.order
        if self.pos_page is not None:
            result['pos_page'] = self.pos_page
        if self.pos_x is not None:
            result['pos_x'] = self.pos_x
        if self.pos_y is not None:
            result['pos_y'] = self.pos_y
        if self.seal_file_key is not None:
            result['seal_file_key'] = self.seal_file_key
        if self.seal_id is not None:
            result['seal_id'] = self.seal_id
        if self.seal_type is not None:
            result['seal_type'] = self.seal_type
        if self.signer_account_id is not None:
            result['signer_account_id'] = self.signer_account_id
        if self.signfield_id is not None:
            result['signfield_id'] = self.signfield_id
        if self.sign_type is not None:
            result['sign_type'] = self.sign_type
        if self.status is not None:
            result['status'] = self.status
        if self.status_description is not None:
            result['status_description'] = self.status_description
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actor_indentity_type') is not None:
            self.actor_indentity_type = m.get('actor_indentity_type')
        if m.get('add_time') is not None:
            self.add_time = m.get('add_time')
        if m.get('assigned_posbean') is not None:
            self.assigned_posbean = m.get('assigned_posbean')
        if m.get('assigned_seal') is not None:
            self.assigned_seal = m.get('assigned_seal')
        if m.get('authorized_account_id') is not None:
            self.authorized_account_id = m.get('authorized_account_id')
        if m.get('auto_execute') is not None:
            self.auto_execute = m.get('auto_execute')
        if m.get('execute_failed_reason') is not None:
            self.execute_failed_reason = m.get('execute_failed_reason')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('pos_page') is not None:
            self.pos_page = m.get('pos_page')
        if m.get('pos_x') is not None:
            self.pos_x = m.get('pos_x')
        if m.get('pos_y') is not None:
            self.pos_y = m.get('pos_y')
        if m.get('seal_file_key') is not None:
            self.seal_file_key = m.get('seal_file_key')
        if m.get('seal_id') is not None:
            self.seal_id = m.get('seal_id')
        if m.get('seal_type') is not None:
            self.seal_type = m.get('seal_type')
        if m.get('signer_account_id') is not None:
            self.signer_account_id = m.get('signer_account_id')
        if m.get('signfield_id') is not None:
            self.signfield_id = m.get('signfield_id')
        if m.get('sign_type') is not None:
            self.sign_type = m.get('sign_type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('status_description') is not None:
            self.status_description = m.get('status_description')
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class ContractAccountApplication(TeaModel):
    def __init__(
        self,
        email: str = None,
        id_number: str = None,
        id_type: str = None,
        mobile: str = None,
        name: str = None,
        user_id: str = None,
    ):
        # 邮箱地址，默认空
        self.email = email
        # 证件号
        self.id_number = id_number
        # 目前仅支持CRED_PSN_CH_IDCARD，即身份证号码
        self.id_type = id_type
        # 手机号码，默认空
        self.mobile = mobile
        # 姓名
        self.name = name
        # 用户唯一标识，可传入第三方平台的个人用户id等
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.id_number, 'id_number')
        self.validate_required(self.id_type, 'id_type')
        self.validate_required(self.name, 'name')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = dict()
        if self.email is not None:
            result['email'] = self.email
        if self.id_number is not None:
            result['id_number'] = self.id_number
        if self.id_type is not None:
            result['id_type'] = self.id_type
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('id_number') is not None:
            self.id_number = m.get('id_number')
        if m.get('id_type') is not None:
            self.id_type = m.get('id_type')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class ContractSignFlowConfig(TeaModel):
    def __init__(
        self,
        notice_developer_url: str = None,
        notice_type: str = None,
        redirect_url: str = None,
        sign_platform: str = None,
        redirect_url_on_failure: str = None,
        free_signature: bool = None,
    ):
        # 回调通知地址 ,默认取项目配置通知地址
        self.notice_developer_url = notice_developer_url
        # 通知方式，逗号分割，1-短信，2-邮件 。默认值1，请务必请选择一个通知方式，否则客户将接收不到流程的签署通知和审批通知，如果流程需要审批，将导致审批无法完成；如果客户需要不通知，可以设置notice_type为""
        self.notice_type = notice_type
        # 签署成功或者流程结束后的默认重定向地址，默认签署完成停在当前页面
        self.redirect_url = redirect_url
        # 签署平台，逗号分割，1-开放服务h5，2-支付宝签 ，默认值1
        self.sign_platform = sign_platform
        # 签署失败时的跳转地址，如果不做单独配置，默认与redirect_url一致（配合twc.notary.contract.signflow.create接口使用）
        self.redirect_url_on_failure = redirect_url_on_failure
        # 是否允许自由签署，默认false（配合twc.notary.contract.signflow.create接口使用）
        self.free_signature = free_signature

    def validate(self):
        self.validate_required(self.notice_type, 'notice_type')

    def to_map(self):
        result = dict()
        if self.notice_developer_url is not None:
            result['notice_developer_url'] = self.notice_developer_url
        if self.notice_type is not None:
            result['notice_type'] = self.notice_type
        if self.redirect_url is not None:
            result['redirect_url'] = self.redirect_url
        if self.sign_platform is not None:
            result['sign_platform'] = self.sign_platform
        if self.redirect_url_on_failure is not None:
            result['redirect_url_on_failure'] = self.redirect_url_on_failure
        if self.free_signature is not None:
            result['free_signature'] = self.free_signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('notice_developer_url') is not None:
            self.notice_developer_url = m.get('notice_developer_url')
        if m.get('notice_type') is not None:
            self.notice_type = m.get('notice_type')
        if m.get('redirect_url') is not None:
            self.redirect_url = m.get('redirect_url')
        if m.get('sign_platform') is not None:
            self.sign_platform = m.get('sign_platform')
        if m.get('redirect_url_on_failure') is not None:
            self.redirect_url_on_failure = m.get('redirect_url_on_failure')
        if m.get('free_signature') is not None:
            self.free_signature = m.get('free_signature')
        return self


class LeaseIotItemInfo(TeaModel):
    def __init__(
        self,
        date: str = None,
        tx_hash: str = None,
        raw_data: str = None,
    ):
        # 证据的时间
        self.date = date
        # 证据的txHash
        self.tx_hash = tx_hash
        # 证据的原始数据，默认为空或加密状态，除非调用方为授权用户（如出资方等
        self.raw_data = raw_data

    def validate(self):
        self.validate_required(self.date, 'date')
        if self.date is not None:
            self.validate_pattern(self.date, 'date', '\\d{4}[-]\\d{1,2}[-]\\d{1,2}[T]\\d{2}:\\d{2}:\\d{2}([Z]|([\\.]\\d{1,9})?[\\+]\\d{2}[\\:]?\\d{2})')
        self.validate_required(self.tx_hash, 'tx_hash')
        self.validate_required(self.raw_data, 'raw_data')

    def to_map(self):
        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        if self.raw_data is not None:
            result['raw_data'] = self.raw_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        if m.get('raw_data') is not None:
            self.raw_data = m.get('raw_data')
        return self


class CertificateInfo(TeaModel):
    def __init__(
        self,
        hash: str = None,
        resource_name: str = None,
        resource_url: str = None,
    ):
        # 存证证明的证书内容的SHA256哈希值
        self.hash = hash
        # 存证证明的证书文件名
        self.resource_name = resource_name
        # 存证证明的证书下载地址
        self.resource_url = resource_url

    def validate(self):
        self.validate_required(self.hash, 'hash')
        self.validate_required(self.resource_name, 'resource_name')
        self.validate_required(self.resource_url, 'resource_url')

    def to_map(self):
        result = dict()
        if self.hash is not None:
            result['hash'] = self.hash
        if self.resource_name is not None:
            result['resource_name'] = self.resource_name
        if self.resource_url is not None:
            result['resource_url'] = self.resource_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hash') is not None:
            self.hash = m.get('hash')
        if m.get('resource_name') is not None:
            self.resource_name = m.get('resource_name')
        if m.get('resource_url') is not None:
            self.resource_url = m.get('resource_url')
        return self


class OneStepSignField(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        file_id: str = None,
        order: int = None,
        pos_page: str = None,
        pos_x: str = None,
        pos_y: str = None,
        seal_id: str = None,
        sign_date_bean_type: int = None,
        sign_date_font_size: int = None,
        sign_date_format: str = None,
        sign_date_pos_page: int = None,
        sign_date_pos_x: str = None,
        sign_date_pos_y: str = None,
        sign_type: int = None,
        third_order_no: str = None,
        width: str = None,
        auto_execute: bool = None,
    ):
        # 签署操作人个人账号标识，即操作本次签署的个人
        self.account_id = account_id
        # 电子合同文件ID
        self.file_id = file_id
        # 签署区顺序，默认1,且不小于1，顺序越小越先处理
        self.order = order
        # 页码信息，当签署区signType为2时, 页码可以'-'分割, 其他情况只能是数字
        self.pos_page = pos_page
        # x坐标
        self.pos_x = pos_x
        # y坐标
        self.pos_y = pos_y
        # 印章id
        self.seal_id = seal_id
        # 是否需要添加签署日期，0-禁止 1-必须 2-不限制，默认0
        self.sign_date_bean_type = sign_date_bean_type
        # 签章日期字体大小,默认12
        self.sign_date_font_size = sign_date_font_size
        # 签章日期格式，yyyy年MM月dd日
        self.sign_date_format = sign_date_format
        # 页码信息，当signDateBeanType为1时，代表签署的印章必须展示签署日期，默认放在印章正下方，签署人可拖拽日期到当前页面的其他位置，如果发起方指定签署位置的同时，需要同时指定日期盖章位置，则需传入日期盖章页码（与印章页码相同），在传入X\Y坐标即可。
        self.sign_date_pos_page = sign_date_pos_page
        # 签章日期x坐标，默认0
        self.sign_date_pos_x = sign_date_pos_x
        # 签章日期y坐标，默认0
        self.sign_date_pos_y = sign_date_pos_y
        # 签署类型，0-不限，1-单页签署，2-骑缝签署，默认1
        self.sign_type = sign_type
        # 第三方业务流水号id，保证相同签署人、相同签约主体、相同签署顺序的任务，对应的第三方业务流水id唯一，默认空
        self.third_order_no = third_order_no
        # 签署区宽，默认印章宽度
        self.width = width
        # 是否自动执行签署，默认false，false-手动签署，true-自动签署
        self.auto_execute = auto_execute

    def validate(self):
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.file_id, 'file_id')
        self.validate_required(self.pos_page, 'pos_page')
        self.validate_required(self.pos_x, 'pos_x')
        self.validate_required(self.pos_y, 'pos_y')

    def to_map(self):
        result = dict()
        if self.account_id is not None:
            result['account_id'] = self.account_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.order is not None:
            result['order'] = self.order
        if self.pos_page is not None:
            result['pos_page'] = self.pos_page
        if self.pos_x is not None:
            result['pos_x'] = self.pos_x
        if self.pos_y is not None:
            result['pos_y'] = self.pos_y
        if self.seal_id is not None:
            result['seal_id'] = self.seal_id
        if self.sign_date_bean_type is not None:
            result['sign_date_bean_type'] = self.sign_date_bean_type
        if self.sign_date_font_size is not None:
            result['sign_date_font_size'] = self.sign_date_font_size
        if self.sign_date_format is not None:
            result['sign_date_format'] = self.sign_date_format
        if self.sign_date_pos_page is not None:
            result['sign_date_pos_page'] = self.sign_date_pos_page
        if self.sign_date_pos_x is not None:
            result['sign_date_pos_x'] = self.sign_date_pos_x
        if self.sign_date_pos_y is not None:
            result['sign_date_pos_y'] = self.sign_date_pos_y
        if self.sign_type is not None:
            result['sign_type'] = self.sign_type
        if self.third_order_no is not None:
            result['third_order_no'] = self.third_order_no
        if self.width is not None:
            result['width'] = self.width
        if self.auto_execute is not None:
            result['auto_execute'] = self.auto_execute
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('account_id') is not None:
            self.account_id = m.get('account_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('pos_page') is not None:
            self.pos_page = m.get('pos_page')
        if m.get('pos_x') is not None:
            self.pos_x = m.get('pos_x')
        if m.get('pos_y') is not None:
            self.pos_y = m.get('pos_y')
        if m.get('seal_id') is not None:
            self.seal_id = m.get('seal_id')
        if m.get('sign_date_bean_type') is not None:
            self.sign_date_bean_type = m.get('sign_date_bean_type')
        if m.get('sign_date_font_size') is not None:
            self.sign_date_font_size = m.get('sign_date_font_size')
        if m.get('sign_date_format') is not None:
            self.sign_date_format = m.get('sign_date_format')
        if m.get('sign_date_pos_page') is not None:
            self.sign_date_pos_page = m.get('sign_date_pos_page')
        if m.get('sign_date_pos_x') is not None:
            self.sign_date_pos_x = m.get('sign_date_pos_x')
        if m.get('sign_date_pos_y') is not None:
            self.sign_date_pos_y = m.get('sign_date_pos_y')
        if m.get('sign_type') is not None:
            self.sign_type = m.get('sign_type')
        if m.get('third_order_no') is not None:
            self.third_order_no = m.get('third_order_no')
        if m.get('width') is not None:
            self.width = m.get('width')
        if m.get('auto_execute') is not None:
            self.auto_execute = m.get('auto_execute')
        return self


class WitnessSignResult(TeaModel):
    def __init__(
        self,
        sign_result: str = None,
        signlog_id: str = None,
        third_doc_id: str = None,
    ):
        # 签名结果，外部用户签署返回
        self.sign_result = sign_result
        # 签署日志id，外部用户签署返回
        self.signlog_id = signlog_id
        # 第三方文档id
        self.third_doc_id = third_doc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sign_result is not None:
            result['sign_result'] = self.sign_result
        if self.signlog_id is not None:
            result['signlog_id'] = self.signlog_id
        if self.third_doc_id is not None:
            result['third_doc_id'] = self.third_doc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sign_result') is not None:
            self.sign_result = m.get('sign_result')
        if m.get('signlog_id') is not None:
            self.signlog_id = m.get('signlog_id')
        if m.get('third_doc_id') is not None:
            self.third_doc_id = m.get('third_doc_id')
        return self


class MediationCaseDetailInfo(TeaModel):
    def __init__(
        self,
        case_number: str = None,
        case_code: str = None,
        cause_action_name: str = None,
        case_tatus: str = None,
        mediation_platform: str = None,
        mediation_org: str = None,
        mediator: str = None,
        apply_time: int = None,
        mediation_result: str = None,
        accuser_intent_amount: int = None,
        accused_intent_amount: int = None,
        mediation_amount: int = None,
        confirm_fact: str = None,
        mediation_agreement: str = None,
    ):
        # 案件编码
        self.case_number = case_number
        # 案号
        self.case_code = case_code
        # 案由
        self.cause_action_name = cause_action_name
        # 案件状态
        self.case_tatus = case_tatus
        # 调解平台
        self.mediation_platform = mediation_platform
        # 调解机构
        self.mediation_org = mediation_org
        # 调解员
        self.mediator = mediator
        # 申请时间
        self.apply_time = apply_time
        # 调解结果
        self.mediation_result = mediation_result
        # 申请人意向金额
        self.accuser_intent_amount = accuser_intent_amount
        # 被申请人意向金额
        self.accused_intent_amount = accused_intent_amount
        # 和解金额
        self.mediation_amount = mediation_amount
        # 已确认事实
        self.confirm_fact = confirm_fact
        # 调解协议（已达成调解协议或未达成原因）
        self.mediation_agreement = mediation_agreement

    def validate(self):
        self.validate_required(self.case_number, 'case_number')
        self.validate_required(self.case_code, 'case_code')
        self.validate_required(self.cause_action_name, 'cause_action_name')
        self.validate_required(self.case_tatus, 'case_tatus')
        self.validate_required(self.mediation_platform, 'mediation_platform')
        self.validate_required(self.mediation_org, 'mediation_org')
        self.validate_required(self.mediator, 'mediator')
        self.validate_required(self.apply_time, 'apply_time')
        self.validate_required(self.mediation_result, 'mediation_result')
        self.validate_required(self.accuser_intent_amount, 'accuser_intent_amount')
        self.validate_required(self.accused_intent_amount, 'accused_intent_amount')
        self.validate_required(self.mediation_amount, 'mediation_amount')
        self.validate_required(self.confirm_fact, 'confirm_fact')
        self.validate_required(self.mediation_agreement, 'mediation_agreement')

    def to_map(self):
        result = dict()
        if self.case_number is not None:
            result['case_number'] = self.case_number
        if self.case_code is not None:
            result['case_code'] = self.case_code
        if self.cause_action_name is not None:
            result['cause_action_name'] = self.cause_action_name
        if self.case_tatus is not None:
            result['case_tatus'] = self.case_tatus
        if self.mediation_platform is not None:
            result['mediation_platform'] = self.mediation_platform
        if self.mediation_org is not None:
            result['mediation_org'] = self.mediation_org
        if self.mediator is not None:
            result['mediator'] = self.mediator
        if self.apply_time is not None:
            result['apply_time'] = self.apply_time
        if self.mediation_result is not None:
            result['mediation_result'] = self.mediation_result
        if self.accuser_intent_amount is not None:
            result['accuser_intent_amount'] = self.accuser_intent_amount
        if self.accused_intent_amount is not None:
            result['accused_intent_amount'] = self.accused_intent_amount
        if self.mediation_amount is not None:
            result['mediation_amount'] = self.mediation_amount
        if self.confirm_fact is not None:
            result['confirm_fact'] = self.confirm_fact
        if self.mediation_agreement is not None:
            result['mediation_agreement'] = self.mediation_agreement
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('case_number') is not None:
            self.case_number = m.get('case_number')
        if m.get('case_code') is not None:
            self.case_code = m.get('case_code')
        if m.get('cause_action_name') is not None:
            self.cause_action_name = m.get('cause_action_name')
        if m.get('case_tatus') is not None:
            self.case_tatus = m.get('case_tatus')
        if m.get('mediation_platform') is not None:
            self.mediation_platform = m.get('mediation_platform')
        if m.get('mediation_org') is not None:
            self.mediation_org = m.get('mediation_org')
        if m.get('mediator') is not None:
            self.mediator = m.get('mediator')
        if m.get('apply_time') is not None:
            self.apply_time = m.get('apply_time')
        if m.get('mediation_result') is not None:
            self.mediation_result = m.get('mediation_result')
        if m.get('accuser_intent_amount') is not None:
            self.accuser_intent_amount = m.get('accuser_intent_amount')
        if m.get('accused_intent_amount') is not None:
            self.accused_intent_amount = m.get('accused_intent_amount')
        if m.get('mediation_amount') is not None:
            self.mediation_amount = m.get('mediation_amount')
        if m.get('confirm_fact') is not None:
            self.confirm_fact = m.get('confirm_fact')
        if m.get('mediation_agreement') is not None:
            self.mediation_agreement = m.get('mediation_agreement')
        return self


class ContractNotaryInitInfo(TeaModel):
    def __init__(
        self,
        content: str = None,
        file_num: int = None,
        initiator: str = None,
        signatories: str = None,
        timestamp: str = None,
        tx_hash: str = None,
    ):
        # 本阶段存证内容哈希值
        self.content = content
        # 签署文件份数
        self.file_num = file_num
        # 签署流程发起人ID
        self.initiator = initiator
        # 签署人ID（支持多个，不同ID间用“,”分隔开），由于流程中签署人可后续追加，最终以ContractNotaryFinishInfo中的singatories信息为准。
        self.signatories = signatories
        # 存证阶段发生时间，UNIX时间戳(毫秒)
        self.timestamp = timestamp
        # 存证凭据，仅在批量核验时需要填写
        self.tx_hash = tx_hash

    def validate(self):
        self.validate_required(self.content, 'content')
        self.validate_required(self.file_num, 'file_num')
        self.validate_required(self.initiator, 'initiator')
        self.validate_required(self.timestamp, 'timestamp')

    def to_map(self):
        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.file_num is not None:
            result['file_num'] = self.file_num
        if self.initiator is not None:
            result['initiator'] = self.initiator
        if self.signatories is not None:
            result['signatories'] = self.signatories
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('file_num') is not None:
            self.file_num = m.get('file_num')
        if m.get('initiator') is not None:
            self.initiator = m.get('initiator')
        if m.get('signatories') is not None:
            self.signatories = m.get('signatories')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class ContractTemplateStructComponent(TeaModel):
    def __init__(
        self,
        font: int = None,
        font_size: str = None,
        height: str = None,
        id: str = None,
        key: str = None,
        label: str = None,
        limit: str = None,
        page: int = None,
        required: bool = None,
        text_color: str = None,
        type: int = None,
        width: str = None,
        x: str = None,
        y: str = None,
    ):
        # 填充字体,默认1，1-宋体，2-新宋体,4-黑体，5-楷体
        self.font = font
        # 填充字体大小,默认12
        self.font_size = font_size
        # 输入项组件高度
        self.height = height
        # 输入项组件id，使用时可用id填充，为空时表示添加，不为空时表示修改
        self.id = id
        # 模板下输入项组件唯一标识，使用模板时也可用根据key值填充
        self.key = key
        # 输入项组件显示名称
        self.label = label
        # 输入项组件type=2,type=3时填充格式校验规则;数字格式如：#,#00.0# 日期格式如： yyyy-MM-dd
        self.limit = limit
        # 页码
        self.page = page
        # 是否必填，默认true
        self.required = required
        # 字体颜色，默认#000000黑色
        self.text_color = text_color
        # 输入项组件类型，1-文本，2-数字,3-日期，6-签约区
        self.type = type
        # 输入项组件宽度
        self.width = width
        # x轴坐标，左下角为原点
        self.x = x
        # y轴坐标，左下角为原点
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.font is not None:
            result['font'] = self.font
        if self.font_size is not None:
            result['font_size'] = self.font_size
        if self.height is not None:
            result['height'] = self.height
        if self.id is not None:
            result['id'] = self.id
        if self.key is not None:
            result['key'] = self.key
        if self.label is not None:
            result['label'] = self.label
        if self.limit is not None:
            result['limit'] = self.limit
        if self.page is not None:
            result['page'] = self.page
        if self.required is not None:
            result['required'] = self.required
        if self.text_color is not None:
            result['text_color'] = self.text_color
        if self.type is not None:
            result['type'] = self.type
        if self.width is not None:
            result['width'] = self.width
        if self.x is not None:
            result['x'] = self.x
        if self.y is not None:
            result['y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('font') is not None:
            self.font = m.get('font')
        if m.get('font_size') is not None:
            self.font_size = m.get('font_size')
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('text_color') is not None:
            self.text_color = m.get('text_color')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('width') is not None:
            self.width = m.get('width')
        if m.get('x') is not None:
            self.x = m.get('x')
        if m.get('y') is not None:
            self.y = m.get('y')
        return self


class WitnessFlowConfig(TeaModel):
    def __init__(
        self,
        organ_realname_types: List[int] = None,
        person_realname_types: List[int] = None,
        real_name_cert: bool = None,
        willingness_types: List[int] = None,
    ):
        # 企业实名认证方式,对公打款：1；企业芝麻认证：3；法定代表授权：4；
        self.organ_realname_types = organ_realname_types
        # 个人实名认证方式, 银行四要素：2；芝麻认证-人脸识别：3；微众-人脸识别：4；
        self.person_realname_types = person_realname_types
        # 是否需要实名认证
        self.real_name_cert = real_name_cert
        # 意愿认证方式, 芝麻认证-人脸识别：2；短信验证码：3；微众-人脸识别：4；ukey认证：5；签署密码认证：6；
        self.willingness_types = willingness_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.organ_realname_types is not None:
            result['organ_realname_types'] = self.organ_realname_types
        if self.person_realname_types is not None:
            result['person_realname_types'] = self.person_realname_types
        if self.real_name_cert is not None:
            result['real_name_cert'] = self.real_name_cert
        if self.willingness_types is not None:
            result['willingness_types'] = self.willingness_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('organ_realname_types') is not None:
            self.organ_realname_types = m.get('organ_realname_types')
        if m.get('person_realname_types') is not None:
            self.person_realname_types = m.get('person_realname_types')
        if m.get('real_name_cert') is not None:
            self.real_name_cert = m.get('real_name_cert')
        if m.get('willingness_types') is not None:
            self.willingness_types = m.get('willingness_types')
        return self


class ContractSeal(TeaModel):
    def __init__(
        self,
        alias: str = None,
        create_date: int = None,
        default_flag: bool = None,
        file_key: str = None,
        height: int = None,
        width: int = None,
        seal_id: str = None,
        seal_type: int = None,
        url: str = None,
        seal_biz_type: str = None,
    ):
        # 印章别名
        self.alias = alias
        # 印章创建时间
        self.create_date = create_date
        # 默认印章标识
        self.default_flag = default_flag
        # 印章fileKey
        self.file_key = file_key
        # 印章高度
        self.height = height
        # 印章宽度
        self.width = width
        # 印章id
        self.seal_id = seal_id
        # 印章类型，1-机构模板章，2-个人模板章，3-自定义印章，4-手绘章
        self.seal_type = seal_type
        # 印章下载地址, 有效时间1小时
        self.url = url
        # 印章业务类型，CANCELLATION-作废章，COMMON-其它
        self.seal_biz_type = seal_biz_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.create_date is not None:
            result['create_date'] = self.create_date
        if self.default_flag is not None:
            result['default_flag'] = self.default_flag
        if self.file_key is not None:
            result['file_key'] = self.file_key
        if self.height is not None:
            result['height'] = self.height
        if self.width is not None:
            result['width'] = self.width
        if self.seal_id is not None:
            result['seal_id'] = self.seal_id
        if self.seal_type is not None:
            result['seal_type'] = self.seal_type
        if self.url is not None:
            result['url'] = self.url
        if self.seal_biz_type is not None:
            result['seal_biz_type'] = self.seal_biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('create_date') is not None:
            self.create_date = m.get('create_date')
        if m.get('default_flag') is not None:
            self.default_flag = m.get('default_flag')
        if m.get('file_key') is not None:
            self.file_key = m.get('file_key')
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('width') is not None:
            self.width = m.get('width')
        if m.get('seal_id') is not None:
            self.seal_id = m.get('seal_id')
        if m.get('seal_type') is not None:
            self.seal_type = m.get('seal_type')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('seal_biz_type') is not None:
            self.seal_biz_type = m.get('seal_biz_type')
        return self


class WitnessSignData(TeaModel):
    def __init__(
        self,
        seal_file_keys: List[str] = None,
        seal_ids: List[str] = None,
        sign_hash: str = None,
        sign_pos_data: str = None,
        third_doc_id: str = None,
    ):
        # 印章图片fileKey列表
        self.seal_file_keys = seal_file_keys
        # 印章id列表
        self.seal_ids = seal_ids
        # 待签署文档摘要值，批量签时必传
        self.sign_hash = sign_hash
        # 签署位置信息
        self.sign_pos_data = sign_pos_data
        # 第三方文档id，批量签时必传
        self.third_doc_id = third_doc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.seal_file_keys is not None:
            result['seal_file_keys'] = self.seal_file_keys
        if self.seal_ids is not None:
            result['seal_ids'] = self.seal_ids
        if self.sign_hash is not None:
            result['sign_hash'] = self.sign_hash
        if self.sign_pos_data is not None:
            result['sign_pos_data'] = self.sign_pos_data
        if self.third_doc_id is not None:
            result['third_doc_id'] = self.third_doc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('seal_file_keys') is not None:
            self.seal_file_keys = m.get('seal_file_keys')
        if m.get('seal_ids') is not None:
            self.seal_ids = m.get('seal_ids')
        if m.get('sign_hash') is not None:
            self.sign_hash = m.get('sign_hash')
        if m.get('sign_pos_data') is not None:
            self.sign_pos_data = m.get('sign_pos_data')
        if m.get('third_doc_id') is not None:
            self.third_doc_id = m.get('third_doc_id')
        return self


class ContractPlatformSignFieldApplication(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        order: int = None,
        seal_id: str = None,
        third_order_no: str = None,
        pos_page: str = None,
        pos_x: str = None,
        pos_y: str = None,
        width: str = None,
        add_sign_time: bool = None,
        sign_type: int = None,
    ):
        # 文件file id
        self.file_id = file_id
        # 签署顺序，默认1,且不小于1，顺序越小越先处理
        self.order = order
        # 印章id， 仅限企业公章，暂不支持指定企业法定代表人印章 ，如不传，则采用账号下的默认印章
        self.seal_id = seal_id
        # 第三方业务流水号id，保证相同签署人、相同签约主体、相同签署顺序的任务，对应的第三方业务流水id唯一，默认空
        self.third_order_no = third_order_no
        # 页码信息，当签署区signType为2时, 页码可以'-'分割, 其他情况只能是数字
        self.pos_page = pos_page
        # x坐标，默认空
        self.pos_x = pos_x
        # y坐标
        self.pos_y = pos_y
        # 签署区宽，默认印章宽度
        self.width = width
        # 是否添加签署时间戳， 默认不添加，默认格式 yyyy-MM-dd HH : mm : ss
        self.add_sign_time = add_sign_time
        # 签署类型， 1-单页签署，2-骑缝签署，默认1
        self.sign_type = sign_type

    def validate(self):
        self.validate_required(self.file_id, 'file_id')
        self.validate_required(self.pos_page, 'pos_page')
        self.validate_required(self.pos_y, 'pos_y')

    def to_map(self):
        result = dict()
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.order is not None:
            result['order'] = self.order
        if self.seal_id is not None:
            result['seal_id'] = self.seal_id
        if self.third_order_no is not None:
            result['third_order_no'] = self.third_order_no
        if self.pos_page is not None:
            result['pos_page'] = self.pos_page
        if self.pos_x is not None:
            result['pos_x'] = self.pos_x
        if self.pos_y is not None:
            result['pos_y'] = self.pos_y
        if self.width is not None:
            result['width'] = self.width
        if self.add_sign_time is not None:
            result['add_sign_time'] = self.add_sign_time
        if self.sign_type is not None:
            result['sign_type'] = self.sign_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('seal_id') is not None:
            self.seal_id = m.get('seal_id')
        if m.get('third_order_no') is not None:
            self.third_order_no = m.get('third_order_no')
        if m.get('pos_page') is not None:
            self.pos_page = m.get('pos_page')
        if m.get('pos_x') is not None:
            self.pos_x = m.get('pos_x')
        if m.get('pos_y') is not None:
            self.pos_y = m.get('pos_y')
        if m.get('width') is not None:
            self.width = m.get('width')
        if m.get('add_sign_time') is not None:
            self.add_sign_time = m.get('add_sign_time')
        if m.get('sign_type') is not None:
            self.sign_type = m.get('sign_type')
        return self


class KeywordsPosition(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_index: int = None,
        pos_x: str = None,
        pos_y: str = None,
    ):
        # 关键字
        self.keyword = keyword
        # 页码
        self.page_index = page_index
        # x坐标
        self.pos_x = pos_x
        # y坐标
        self.pos_y = pos_y

    def validate(self):
        self.validate_required(self.keyword, 'keyword')
        self.validate_required(self.page_index, 'page_index')
        self.validate_required(self.pos_x, 'pos_x')
        self.validate_required(self.pos_y, 'pos_y')

    def to_map(self):
        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_index is not None:
            result['page_index'] = self.page_index
        if self.pos_x is not None:
            result['pos_x'] = self.pos_x
        if self.pos_y is not None:
            result['pos_y'] = self.pos_y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('page_index') is not None:
            self.page_index = m.get('page_index')
        if m.get('pos_x') is not None:
            self.pos_x = m.get('pos_x')
        if m.get('pos_y') is not None:
            self.pos_y = m.get('pos_y')
        return self


class WitnessDocs(TeaModel):
    def __init__(
        self,
        doc_hash: str = None,
        third_doc_id: str = None,
    ):
        # 文档摘要值
        self.doc_hash = doc_hash
        # 第三方文档id
        self.third_doc_id = third_doc_id

    def validate(self):
        self.validate_required(self.doc_hash, 'doc_hash')
        self.validate_required(self.third_doc_id, 'third_doc_id')

    def to_map(self):
        result = dict()
        if self.doc_hash is not None:
            result['doc_hash'] = self.doc_hash
        if self.third_doc_id is not None:
            result['third_doc_id'] = self.third_doc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('doc_hash') is not None:
            self.doc_hash = m.get('doc_hash')
        if m.get('third_doc_id') is not None:
            self.third_doc_id = m.get('third_doc_id')
        return self


class RepaymentOrderRequest(TeaModel):
    def __init__(
        self,
        pay_date: int = None,
        pay_money: int = None,
        trigger_immediately: int = None,
    ):
        # 代扣触发时间，精确到毫秒
        # java.lang.System#currentTimeMillis()
        self.pay_date = pay_date
        # 代扣金额，整数 精确到分
        self.pay_money = pay_money
        # 是否用户签署成功后立即触发第一期代扣
        self.trigger_immediately = trigger_immediately

    def validate(self):
        self.validate_required(self.pay_date, 'pay_date')
        self.validate_required(self.pay_money, 'pay_money')

    def to_map(self):
        result = dict()
        if self.pay_date is not None:
            result['pay_date'] = self.pay_date
        if self.pay_money is not None:
            result['pay_money'] = self.pay_money
        if self.trigger_immediately is not None:
            result['trigger_immediately'] = self.trigger_immediately
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pay_date') is not None:
            self.pay_date = m.get('pay_date')
        if m.get('pay_money') is not None:
            self.pay_money = m.get('pay_money')
        if m.get('trigger_immediately') is not None:
            self.trigger_immediately = m.get('trigger_immediately')
        return self


class TsrResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        hashed_message: str = None,
        hash_algorithm: str = None,
        message: str = None,
        ts: str = None,
        ctsr: str = None,
        sn: str = None,
    ):
        # 可信时间请求结果状态吗
        self.code = code
        # hash后的信息
        self.hashed_message = hashed_message
        # 哈希算法
        self.hash_algorithm = hash_algorithm
        # 请求失败时候的错误信息
        self.message = message
        # 时间
        self.ts = ts
        # 精简后的时间戳完整编码（在校验时需要提交）
        self.ctsr = ctsr
        # 凭证序列号 （在校验的时需要先填写凭证编号）
        # 
        self.sn = sn

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.hashed_message, 'hashed_message')
        self.validate_required(self.hash_algorithm, 'hash_algorithm')
        self.validate_required(self.ts, 'ts')
        self.validate_required(self.ctsr, 'ctsr')
        self.validate_required(self.sn, 'sn')

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.hashed_message is not None:
            result['hashed_message'] = self.hashed_message
        if self.hash_algorithm is not None:
            result['hash_algorithm'] = self.hash_algorithm
        if self.message is not None:
            result['message'] = self.message
        if self.ts is not None:
            result['ts'] = self.ts
        if self.ctsr is not None:
            result['ctsr'] = self.ctsr
        if self.sn is not None:
            result['sn'] = self.sn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('hashed_message') is not None:
            self.hashed_message = m.get('hashed_message')
        if m.get('hash_algorithm') is not None:
            self.hash_algorithm = m.get('hash_algorithm')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('ts') is not None:
            self.ts = m.get('ts')
        if m.get('ctsr') is not None:
            self.ctsr = m.get('ctsr')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        return self


class CallbackArbitrationStatusRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        acceptance_number: str = None,
        case_no: str = None,
        confirm_time: int = None,
        preacceptance_number: str = None,
        send_time: int = None,
        status: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 案件文书号
        self.acceptance_number = acceptance_number
        # 案件编号
        self.case_no = case_no
        # 确认时间时间戳
        self.confirm_time = confirm_time
        # 预处理案号
        self.preacceptance_number = preacceptance_number
        # 发送时间时间戳
        self.send_time = send_time
        # 案件状态
        self.status = status

    def validate(self):
        self.validate_required(self.case_no, 'case_no')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.acceptance_number is not None:
            result['acceptance_number'] = self.acceptance_number
        if self.case_no is not None:
            result['case_no'] = self.case_no
        if self.confirm_time is not None:
            result['confirm_time'] = self.confirm_time
        if self.preacceptance_number is not None:
            result['preacceptance_number'] = self.preacceptance_number
        if self.send_time is not None:
            result['send_time'] = self.send_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('acceptance_number') is not None:
            self.acceptance_number = m.get('acceptance_number')
        if m.get('case_no') is not None:
            self.case_no = m.get('case_no')
        if m.get('confirm_time') is not None:
            self.confirm_time = m.get('confirm_time')
        if m.get('preacceptance_number') is not None:
            self.preacceptance_number = m.get('preacceptance_number')
        if m.get('send_time') is not None:
            self.send_time = m.get('send_time')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class CallbackArbitrationStatusResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        return self


class CreateContractAccountRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        email: str = None,
        id_number: str = None,
        id_type: str = None,
        mobile: str = None,
        name: str = None,
        user_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 邮箱地址，默认空
        self.email = email
        # 证件号
        self.id_number = id_number
        # 证件类型，默认CRED_PSN_CH_IDCARD，详见个人证件类型说明文档（https://tech.antfin.com/docs/2/155166）
        self.id_type = id_type
        # 手机号码，默认空
        self.mobile = mobile
        # 姓名
        self.name = name
        # 用户唯一标识，可传入第三方平台的个人用户id、证件号、手机号、邮箱等，如果设置则作为账号唯一性字段，相同信息不可重复创建。（个人用户与机构的唯一标识不可重复）
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.id_number, 'id_number')
        self.validate_required(self.id_type, 'id_type')
        self.validate_required(self.name, 'name')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.email is not None:
            result['email'] = self.email
        if self.id_number is not None:
            result['id_number'] = self.id_number
        if self.id_type is not None:
            result['id_type'] = self.id_type
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('id_number') is not None:
            self.id_number = m.get('id_number')
        if m.get('id_type') is not None:
            self.id_type = m.get('id_type')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class CreateContractAccountResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        account_id: str = None,
        code: int = None,
        message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 个人账号ID
        self.account_id = account_id
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.account_id is not None:
            result['account_id'] = self.account_id
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('account_id') is not None:
            self.account_id = m.get('account_id')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateContractAccountsealRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        account_id: str = None,
        alias: str = None,
        color: str = None,
        height: int = None,
        width: int = None,
        type: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 电子合同用户ID（在twc.notary.contract.account.create接口中创建）
        self.account_id = account_id
        # 印章别名
        self.alias = alias
        # 印章颜色，RED-红色， BLUE-蓝色，BLACK-黑色
        self.color = color
        # 印章高度, 默认95px
        self.height = height
        # 印章宽度, 默认95px
        self.width = width
        # 模板类型, 详见个人印章样式说明 SQUARE, BORDERLESS, FZKC, HWLS, HWXK, HWXKBORDER, HYLSF, RECTANGLE, YGYJFCS, YGYMBXS, YYGXSF
        self.type = type

    def validate(self):
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.color, 'color')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.account_id is not None:
            result['account_id'] = self.account_id
        if self.alias is not None:
            result['alias'] = self.alias
        if self.color is not None:
            result['color'] = self.color
        if self.height is not None:
            result['height'] = self.height
        if self.width is not None:
            result['width'] = self.width
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('account_id') is not None:
            self.account_id = m.get('account_id')
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('color') is not None:
            self.color = m.get('color')
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('width') is not None:
            self.width = m.get('width')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateContractAccountsealResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        file_key: str = None,
        seal_id: str = None,
        url: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message
        # 印章fileKey
        self.file_key = file_key
        # 印章id
        self.seal_id = seal_id
        # 印章下载地址, 有效时间1小时
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.file_key is not None:
            result['file_key'] = self.file_key
        if self.seal_id is not None:
            result['seal_id'] = self.seal_id
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('file_key') is not None:
            self.file_key = m.get('file_key')
        if m.get('seal_id') is not None:
            self.seal_id = m.get('seal_id')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class CreateContractOrganizationRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        creator: str = None,
        id_number: str = None,
        id_type: str = None,
        legal_person: str = None,
        legal_person_id: str = None,
        name: str = None,
        user_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 创建人个人账号ID，也就是调用个人账号创建接口（twc.notary.contract.account.create
        # ）返回的accountId
        self.creator = creator
        # 证件号
        self.id_number = id_number
        # 证件类型，默认CRED_ORG_USCC，详见机构证件类型说明 （https://tech.antfin.com/docs/2/155166）
        self.id_type = id_type
        # 企业法人名称
        self.legal_person = legal_person
        # 企业法人证件号
        self.legal_person_id = legal_person_id
        # 机构名称
        self.name = name
        # 机构唯一标识，可传入第三方平台机构id、企业证件号、企业邮箱等如果设置则作为账号唯一性字段，相同id不可重复创建。（个人用户与机构的唯一标识不可重复）
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.creator, 'creator')
        self.validate_required(self.id_number, 'id_number')
        self.validate_required(self.id_type, 'id_type')
        self.validate_required(self.name, 'name')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.creator is not None:
            result['creator'] = self.creator
        if self.id_number is not None:
            result['id_number'] = self.id_number
        if self.id_type is not None:
            result['id_type'] = self.id_type
        if self.legal_person is not None:
            result['legal_person'] = self.legal_person
        if self.legal_person_id is not None:
            result['legal_person_id'] = self.legal_person_id
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('id_number') is not None:
            self.id_number = m.get('id_number')
        if m.get('id_type') is not None:
            self.id_type = m.get('id_type')
        if m.get('legal_person') is not None:
            self.legal_person = m.get('legal_person')
        if m.get('legal_person_id') is not None:
            self.legal_person_id = m.get('legal_person_id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class CreateContractOrganizationResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        org_id: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message
        # 机构账号ID
        self.org_id = org_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.org_id is not None:
            result['org_id'] = self.org_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('org_id') is not None:
            self.org_id = m.get('org_id')
        return self


class CreateContractOrgsealRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        alias: str = None,
        central: str = None,
        color: str = None,
        height: int = None,
        htext: str = None,
        org_id: str = None,
        qtext: str = None,
        type: str = None,
        width: int = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 印章别名
        self.alias = alias
        # 中心图案类型，STAR-圆形有五角星，NONE-圆形无五角星， 详见机构印章样式说明
        self.central = central
        # 印章颜色，RED-红色，BLUE-蓝色，BLACK-黑色
        self.color = color
        # 印章高度，默认159px
        self.height = height
        # 横向文，可设置0-8个字，企业名称超出25个字后，不支持设置横向文
        self.htext = htext
        # 机构ID
        self.org_id = org_id
        # 下弦文，可设置0-20个字，企业企业名称超出25个字后，不支持设置下弦文
        self.qtext = qtext
        # 模板类型，TEMPLATE_ROUND-圆章，TEMPLATE_OVAL-椭圆章， 详见机构印章样式说明
        self.type = type
        # 印章宽度，默认159px
        self.width = width

    def validate(self):
        self.validate_required(self.central, 'central')
        self.validate_required(self.color, 'color')
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.alias is not None:
            result['alias'] = self.alias
        if self.central is not None:
            result['central'] = self.central
        if self.color is not None:
            result['color'] = self.color
        if self.height is not None:
            result['height'] = self.height
        if self.htext is not None:
            result['htext'] = self.htext
        if self.org_id is not None:
            result['org_id'] = self.org_id
        if self.qtext is not None:
            result['qtext'] = self.qtext
        if self.type is not None:
            result['type'] = self.type
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('central') is not None:
            self.central = m.get('central')
        if m.get('color') is not None:
            self.color = m.get('color')
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('htext') is not None:
            self.htext = m.get('htext')
        if m.get('org_id') is not None:
            self.org_id = m.get('org_id')
        if m.get('qtext') is not None:
            self.qtext = m.get('qtext')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class CreateContractOrgsealResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        file_key: str = None,
        message: str = None,
        seal_id: str = None,
        url: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 印章fileKey
        self.file_key = file_key
        # 业务码信息
        self.message = message
        # 印章ID
        self.seal_id = seal_id
        # 印章下载地址, 有效时间1小时
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.file_key is not None:
            result['file_key'] = self.file_key
        if self.message is not None:
            result['message'] = self.message
        if self.seal_id is not None:
            result['seal_id'] = self.seal_id
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('file_key') is not None:
            self.file_key = m.get('file_key')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('seal_id') is not None:
            self.seal_id = m.get('seal_id')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class AuthContractSignRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        account_id: str = None,
        deadline: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 授权人ID，即个人账号ID或机构账号ID
        self.account_id = account_id
        # 授权截止时间, 格式为yyyy-MM-dd HH:mm:ss，默认无限期
        self.deadline = deadline

    def validate(self):
        self.validate_required(self.account_id, 'account_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.account_id is not None:
            result['account_id'] = self.account_id
        if self.deadline is not None:
            result['deadline'] = self.deadline
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('account_id') is not None:
            self.account_id = m.get('account_id')
        if m.get('deadline') is not None:
            self.deadline = m.get('deadline')
        return self


class AuthContractSignResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        accepted: bool = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message
        # 业务数据, 是否授权成功
        self.accepted = accepted

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.accepted is not None:
            result['accepted'] = self.accepted
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('accepted') is not None:
            self.accepted = m.get('accepted')
        return self


class CreateContractTemplateRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        content_md_5: str = None,
        content_type: str = None,
        convert_2pdf: bool = None,
        file_name: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 模板文件md5值，再做base64编码
        self.content_md_5 = content_md_5
        # 目标文件的MIME类型
        self.content_type = content_type
        # 是否需要转成pdf，如果模板文件为.doc/.docx 传true，为pdf传false
        self.convert_2pdf = convert_2pdf
        # 文件名称，必须带扩展名如:.pdf,.doc,.docx
        self.file_name = file_name

    def validate(self):
        self.validate_required(self.content_md_5, 'content_md_5')
        self.validate_required(self.content_type, 'content_type')
        self.validate_required(self.convert_2pdf, 'convert_2pdf')
        self.validate_required(self.file_name, 'file_name')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.content_md_5 is not None:
            result['content_md5'] = self.content_md_5
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.convert_2pdf is not None:
            result['convert2_pdf'] = self.convert_2pdf
        if self.file_name is not None:
            result['file_name'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('content_md5') is not None:
            self.content_md_5 = m.get('content_md5')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('convert2_pdf') is not None:
            self.convert_2pdf = m.get('convert2_pdf')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        return self


class CreateContractTemplateResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        template_id: str = None,
        upload_url: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message
        # 模板ID
        self.template_id = template_id
        # 文件直传地址，需要用此上传地址使用put方式上传文件，只有文件上传后模板才可用
        self.upload_url = upload_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.template_id is not None:
            result['template_id'] = self.template_id
        if self.upload_url is not None:
            result['upload_url'] = self.upload_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')
        if m.get('upload_url') is not None:
            self.upload_url = m.get('upload_url')
        return self


class CreateContractFlowRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        auto_archive: bool = None,
        business_scene: str = None,
        config_info: ContractSignFlowConfig = None,
        contract_remind: int = None,
        contract_validity: int = None,
        initiator_account_id: str = None,
        initiator_authorized_account_id: str = None,
        sign_validity: int = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 是否自动归档，默认false。如设置为true，则在调用签署流程开启(twc.notary.contract.flow.start)后，当所有签署人签署完毕，系统自动将流程归档，状态变为“已完成”状态，在流程状态为“已完成”前，可随时添加签署人；如设置为false，则在调用签署流程开启后，需主动调用签署流程归档接口，将流程状态变更为“已完成”，归档前可随时添加签署人；已完成的流程才可下载签署后的文件
        self.auto_archive = auto_archive
        # 文件主题
        self.business_scene = business_scene
        # 任务配置信息
        self.config_info = config_info
        # 文件到期前，提前多久回调提醒续签，单位为小时，时间区间：1小时——15天（360小时），默认不提醒
        self.contract_remind = contract_remind
        # 文件有效截止日期,毫秒，默认不失效
        self.contract_validity = contract_validity
        # 发起人账户id，即发起本次签署的操作人个人账号id；如不传，默认由对接平台发起
        self.initiator_account_id = initiator_account_id
        # 发起方主体id，如存在个人代机构发起签约，则需传入机构id；如不传，则默认是对接平台
        self.initiator_authorized_account_id = initiator_authorized_account_id
        # 签署有效截止日期,毫秒，默认不失效
        self.sign_validity = sign_validity

    def validate(self):
        self.validate_required(self.business_scene, 'business_scene')
        if self.config_info:
            self.config_info.validate()

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.auto_archive is not None:
            result['auto_archive'] = self.auto_archive
        if self.business_scene is not None:
            result['business_scene'] = self.business_scene
        if self.config_info is not None:
            result['config_info'] = self.config_info.to_map()
        if self.contract_remind is not None:
            result['contract_remind'] = self.contract_remind
        if self.contract_validity is not None:
            result['contract_validity'] = self.contract_validity
        if self.initiator_account_id is not None:
            result['initiator_account_id'] = self.initiator_account_id
        if self.initiator_authorized_account_id is not None:
            result['initiator_authorized_account_id'] = self.initiator_authorized_account_id
        if self.sign_validity is not None:
            result['sign_validity'] = self.sign_validity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('auto_archive') is not None:
            self.auto_archive = m.get('auto_archive')
        if m.get('business_scene') is not None:
            self.business_scene = m.get('business_scene')
        if m.get('config_info') is not None:
            temp_model = ContractSignFlowConfig()
            self.config_info = temp_model.from_map(m['config_info'])
        if m.get('contract_remind') is not None:
            self.contract_remind = m.get('contract_remind')
        if m.get('contract_validity') is not None:
            self.contract_validity = m.get('contract_validity')
        if m.get('initiator_account_id') is not None:
            self.initiator_account_id = m.get('initiator_account_id')
        if m.get('initiator_authorized_account_id') is not None:
            self.initiator_authorized_account_id = m.get('initiator_authorized_account_id')
        if m.get('sign_validity') is not None:
            self.sign_validity = m.get('sign_validity')
        return self


class CreateContractFlowResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        flow_id: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message
        # 流程ID
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        return self


class AddContractDocumentRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        flow_id: str = None,
        docs: List[ContractDoc] = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 流程ID
        self.flow_id = flow_id
        # 文档列表数据
        self.docs = docs

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')
        self.validate_required(self.docs, 'docs')
        if self.docs:
            for k in self.docs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        result['docs'] = []
        if self.docs is not None:
            for k in self.docs:
                result['docs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        self.docs = []
        if m.get('docs') is not None:
            for k in m.get('docs'):
                temp_model = ContractDoc()
                self.docs.append(temp_model.from_map(k))
        return self


class AddContractDocumentResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class AddContractSignfieldRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        flow_id: str = None,
        signfields: List[ContractSignFieldApplication] = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 签署流程ID
        self.flow_id = flow_id
        # 签署区列表数据
        self.signfields = signfields

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')
        self.validate_required(self.signfields, 'signfields')
        if self.signfields:
            for k in self.signfields:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        result['signfields'] = []
        if self.signfields is not None:
            for k in self.signfields:
                result['signfields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        self.signfields = []
        if m.get('signfields') is not None:
            for k in m.get('signfields'):
                temp_model = ContractSignFieldApplication()
                self.signfields.append(temp_model.from_map(k))
        return self


class AddContractSignfieldResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        signfields: List[ContractSignField] = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message
        # 签署区列表数据
        self.signfields = signfields

    def validate(self):
        if self.signfields:
            for k in self.signfields:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        result['signfields'] = []
        if self.signfields is not None:
            for k in self.signfields:
                result['signfields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        self.signfields = []
        if m.get('signfields') is not None:
            for k in m.get('signfields'):
                temp_model = ContractSignField()
                self.signfields.append(temp_model.from_map(k))
        return self


class StartContractFlowRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        flow_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 流程ID
        self.flow_id = flow_id

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        return self


class StartContractFlowResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class SaveContractFlowRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        flow_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 流程ID
        self.flow_id = flow_id

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        return self


class SaveContractFlowResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DownloadContractDocumentRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        flow_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 流程ID
        self.flow_id = flow_id

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        return self


class DownloadContractDocumentResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        docs: List[ContractDocAddress] = None,
        message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 文档下载地址信息列表
        self.docs = docs
        # 业务码信息
        self.message = message

    def validate(self):
        if self.docs:
            for k in self.docs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        result['docs'] = []
        if self.docs is not None:
            for k in self.docs:
                result['docs'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        self.docs = []
        if m.get('docs') is not None:
            for k in m.get('docs'):
                temp_model = ContractDocAddress()
                self.docs.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class AddContractFileRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        name: str = None,
        template_id: str = None,
        simple_form_fields: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 文件名称
        self.name = name
        # 模板编号
        self.template_id = template_id
        # 输入项填充内容，以key:value传入
        self.simple_form_fields = simple_form_fields

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.template_id, 'template_id')
        self.validate_required(self.simple_form_fields, 'simple_form_fields')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.name is not None:
            result['name'] = self.name
        if self.template_id is not None:
            result['template_id'] = self.template_id
        if self.simple_form_fields is not None:
            result['simple_form_fields'] = self.simple_form_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')
        if m.get('simple_form_fields') is not None:
            self.simple_form_fields = m.get('simple_form_fields')
        return self


class AddContractFileResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        download_url: str = None,
        file_id: str = None,
        file_name: str = None,
        code: int = None,
        message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 文件下载地址，有效期一小时
        self.download_url = download_url
        # 文件id
        self.file_id = file_id
        # 文件名称
        self.file_name = file_name
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.file_name is not None:
            result['file_name'] = self.file_name
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateContractPlatformRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        creator: ContractAccountApplication = None,
        platform: ContractOrganizationApplication = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 平台方经办人信息
        self.creator = creator
        # 平台机构信息
        self.platform = platform

    def validate(self):
        self.validate_required(self.creator, 'creator')
        if self.creator:
            self.creator.validate()
        self.validate_required(self.platform, 'platform')
        if self.platform:
            self.platform.validate()

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.creator is not None:
            result['creator'] = self.creator.to_map()
        if self.platform is not None:
            result['platform'] = self.platform.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('creator') is not None:
            temp_model = ContractAccountApplication()
            self.creator = temp_model.from_map(m['creator'])
        if m.get('platform') is not None:
            temp_model = ContractOrganizationApplication()
            self.platform = temp_model.from_map(m['platform'])
        return self


class CreateContractPlatformResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        creator_id: str = None,
        platform_id: str = None,
        secret: str = None,
        code: int = None,
        message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 创建人ID
        self.creator_id = creator_id
        # 平台方ID
        self.platform_id = platform_id
        # 平台用户与智能合同服务间鉴权使用的密钥
        self.secret = secret
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.creator_id is not None:
            result['creator_id'] = self.creator_id
        if self.platform_id is not None:
            result['platform_id'] = self.platform_id
        if self.secret is not None:
            result['secret'] = self.secret
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('creator_id') is not None:
            self.creator_id = m.get('creator_id')
        if m.get('platform_id') is not None:
            self.platform_id = m.get('platform_id')
        if m.get('secret') is not None:
            self.secret = m.get('secret')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateContractUserRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        organization: ContractOrganizationApplication = None,
        user: ContractAccountApplication = None,
        user_type: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 用户类型为机构时，填写机构信息
        self.organization = organization
        # 用户类型为个人时，则为个人用户信息；用户类型为机构时，则为机构账号经办人信息
        self.user = user
        # 用户类型，个人（PERSON）或机构（ORGANIZATION）
        self.user_type = user_type

    def validate(self):
        if self.organization:
            self.organization.validate()
        self.validate_required(self.user, 'user')
        if self.user:
            self.user.validate()
        self.validate_required(self.user_type, 'user_type')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.organization is not None:
            result['organization'] = self.organization.to_map()
        if self.user is not None:
            result['user'] = self.user.to_map()
        if self.user_type is not None:
            result['user_type'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('organization') is not None:
            temp_model = ContractOrganizationApplication()
            self.organization = temp_model.from_map(m['organization'])
        if m.get('user') is not None:
            temp_model = ContractAccountApplication()
            self.user = temp_model.from_map(m['user'])
        if m.get('user_type') is not None:
            self.user_type = m.get('user_type')
        return self


class CreateContractUserResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        organization_id: str = None,
        user_id: str = None,
        code: int = None,
        message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 机构账号
        self.organization_id = organization_id
        # 用户类型为个人时返回用户账号；用户类型为机构时返回经办人账号
        self.user_id = user_id
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.organization_id is not None:
            result['organization_id'] = self.organization_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('organization_id') is not None:
            self.organization_id = m.get('organization_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class StartContractHandsignRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        agent_account_id: str = None,
        auto_archive: bool = None,
        business_scene: str = None,
        contract_remind: int = None,
        contract_sign_flow_config: ContractSignFlowConfig = None,
        contract_validity: int = None,
        initiator_account_id: str = None,
        initiator_authorized_account_id: str = None,
        repayment_order_info: List[RepaymentOrderRequest] = None,
        sign_platform: str = None,
        sign_validity: str = None,
        simple_form_fields: str = None,
        template: str = None,
        user_account: str = None,
        short_url: bool = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 代理商户账户
        self.agent_account_id = agent_account_id
        # 是否自动归档，默认为true
        self.auto_archive = auto_archive
        # 合同文件主题
        self.business_scene = business_scene
        # 文件到期前，提前多少小时回调提醒续签，小时（时间区间：1小时——15天），默认不提醒
        self.contract_remind = contract_remind
        # 签署流程任务配置信息
        self.contract_sign_flow_config = contract_sign_flow_config
        # 文件有效截止日期,毫秒，默认不失效
        self.contract_validity = contract_validity
        # 发起人账户id，即发起本次签署的操作人个人账号id；如不传，默认由对接平台发起
        self.initiator_account_id = initiator_account_id
        # 发起方主体id，如存在个人代机构发起签约，则需传入机构id；如不传，则默认是对接平台
        # 
        # 
        self.initiator_authorized_account_id = initiator_authorized_account_id
        # 代扣规则详情，不可为空
        self.repayment_order_info = repayment_order_info
        # 签署平台，ALIPAY（支付宝小程序）或H5，默认H5
        self.sign_platform = sign_platform
        # 签署有效截止日期,毫秒，默认不失效
        self.sign_validity = sign_validity
        # 输入项填充内容，以key:value传入
        self.simple_form_fields = simple_form_fields
        # 待签署的智能合同模板ID
        self.template = template
        # 待签署客户的账户ID
        self.user_account = user_account
        # 是否需要短网址
        self.short_url = short_url

    def validate(self):
        self.validate_required(self.business_scene, 'business_scene')
        if self.contract_sign_flow_config:
            self.contract_sign_flow_config.validate()
        if self.repayment_order_info:
            for k in self.repayment_order_info:
                if k:
                    k.validate()
        self.validate_required(self.simple_form_fields, 'simple_form_fields')
        self.validate_required(self.template, 'template')
        self.validate_required(self.user_account, 'user_account')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.agent_account_id is not None:
            result['agent_account_id'] = self.agent_account_id
        if self.auto_archive is not None:
            result['auto_archive'] = self.auto_archive
        if self.business_scene is not None:
            result['business_scene'] = self.business_scene
        if self.contract_remind is not None:
            result['contract_remind'] = self.contract_remind
        if self.contract_sign_flow_config is not None:
            result['contract_sign_flow_config'] = self.contract_sign_flow_config.to_map()
        if self.contract_validity is not None:
            result['contract_validity'] = self.contract_validity
        if self.initiator_account_id is not None:
            result['initiator_account_id'] = self.initiator_account_id
        if self.initiator_authorized_account_id is not None:
            result['initiator_authorized_account_id'] = self.initiator_authorized_account_id
        result['repayment_order_info'] = []
        if self.repayment_order_info is not None:
            for k in self.repayment_order_info:
                result['repayment_order_info'].append(k.to_map() if k else None)
        if self.sign_platform is not None:
            result['sign_platform'] = self.sign_platform
        if self.sign_validity is not None:
            result['sign_validity'] = self.sign_validity
        if self.simple_form_fields is not None:
            result['simple_form_fields'] = self.simple_form_fields
        if self.template is not None:
            result['template'] = self.template
        if self.user_account is not None:
            result['user_account'] = self.user_account
        if self.short_url is not None:
            result['short_url'] = self.short_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('agent_account_id') is not None:
            self.agent_account_id = m.get('agent_account_id')
        if m.get('auto_archive') is not None:
            self.auto_archive = m.get('auto_archive')
        if m.get('business_scene') is not None:
            self.business_scene = m.get('business_scene')
        if m.get('contract_remind') is not None:
            self.contract_remind = m.get('contract_remind')
        if m.get('contract_sign_flow_config') is not None:
            temp_model = ContractSignFlowConfig()
            self.contract_sign_flow_config = temp_model.from_map(m['contract_sign_flow_config'])
        if m.get('contract_validity') is not None:
            self.contract_validity = m.get('contract_validity')
        if m.get('initiator_account_id') is not None:
            self.initiator_account_id = m.get('initiator_account_id')
        if m.get('initiator_authorized_account_id') is not None:
            self.initiator_authorized_account_id = m.get('initiator_authorized_account_id')
        self.repayment_order_info = []
        if m.get('repayment_order_info') is not None:
            for k in m.get('repayment_order_info'):
                temp_model = RepaymentOrderRequest()
                self.repayment_order_info.append(temp_model.from_map(k))
        if m.get('sign_platform') is not None:
            self.sign_platform = m.get('sign_platform')
        if m.get('sign_validity') is not None:
            self.sign_validity = m.get('sign_validity')
        if m.get('simple_form_fields') is not None:
            self.simple_form_fields = m.get('simple_form_fields')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('user_account') is not None:
            self.user_account = m.get('user_account')
        if m.get('short_url') is not None:
            self.short_url = m.get('short_url')
        return self


class StartContractHandsignResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        flow_id: str = None,
        message: str = None,
        url: str = None,
        short_url: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 签署流程ID
        self.flow_id = flow_id
        # 业务码信息
        self.message = message
        # 手动签约唤起地址
        self.url = url
        # 唤起签约地址短网址
        self.short_url = short_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.message is not None:
            result['message'] = self.message
        if self.url is not None:
            result['url'] = self.url
        if self.short_url is not None:
            result['short_url'] = self.short_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('short_url') is not None:
            self.short_url = m.get('short_url')
        return self


class QueryContractFlowRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        flow_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 流程id
        self.flow_id = flow_id

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        return self


class QueryContractFlowResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        auto_archive: bool = None,
        business_scene: str = None,
        code: int = None,
        config_info: ContractSignFlowConfig = None,
        contract_remind: int = None,
        contract_validity: int = None,
        flow_desc: str = None,
        flow_end_time: str = None,
        flow_id: str = None,
        flow_start_time: str = None,
        flow_status: int = None,
        initiator_account_id: str = None,
        initiator_authorized_account_id: str = None,
        message: str = None,
        sign_validity: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 是否自动归档
        self.auto_archive = auto_archive
        # 文件主题
        self.business_scene = business_scene
        # 业务码，0表示成功
        self.code = code
        # 流程配置信息
        self.config_info = config_info
        # 文件到期前，提前多少小时提醒续签
        self.contract_remind = contract_remind
        # 文件有效截止日期
        self.contract_validity = contract_validity
        # 流程描述, 如果流程已拒签或已撤回, 并且存在拒签或撤回原因, 流程描述显示为原因, 否则默认为流程状态描述
        self.flow_desc = flow_desc
        # 流程结束时间
        self.flow_end_time = flow_end_time
        # 流程ID
        self.flow_id = flow_id
        # 流程开始时间
        self.flow_start_time = flow_start_time
        # 流程状态,0-草稿 1-签署中 2-完成 3-撤销 4-终止 5-过期 6-删除 7-拒签
        self.flow_status = flow_status
        # 发起人账户id
        self.initiator_account_id = initiator_account_id
        # 发起方主体id
        self.initiator_authorized_account_id = initiator_authorized_account_id
        # 业务码信息
        self.message = message
        # 签署有效截止日期
        self.sign_validity = sign_validity

    def validate(self):
        if self.config_info:
            self.config_info.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.auto_archive is not None:
            result['auto_archive'] = self.auto_archive
        if self.business_scene is not None:
            result['business_scene'] = self.business_scene
        if self.code is not None:
            result['code'] = self.code
        if self.config_info is not None:
            result['config_info'] = self.config_info.to_map()
        if self.contract_remind is not None:
            result['contract_remind'] = self.contract_remind
        if self.contract_validity is not None:
            result['contract_validity'] = self.contract_validity
        if self.flow_desc is not None:
            result['flow_desc'] = self.flow_desc
        if self.flow_end_time is not None:
            result['flow_end_time'] = self.flow_end_time
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.flow_start_time is not None:
            result['flow_start_time'] = self.flow_start_time
        if self.flow_status is not None:
            result['flow_status'] = self.flow_status
        if self.initiator_account_id is not None:
            result['initiator_account_id'] = self.initiator_account_id
        if self.initiator_authorized_account_id is not None:
            result['initiator_authorized_account_id'] = self.initiator_authorized_account_id
        if self.message is not None:
            result['message'] = self.message
        if self.sign_validity is not None:
            result['sign_validity'] = self.sign_validity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('auto_archive') is not None:
            self.auto_archive = m.get('auto_archive')
        if m.get('business_scene') is not None:
            self.business_scene = m.get('business_scene')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('config_info') is not None:
            temp_model = ContractSignFlowConfig()
            self.config_info = temp_model.from_map(m['config_info'])
        if m.get('contract_remind') is not None:
            self.contract_remind = m.get('contract_remind')
        if m.get('contract_validity') is not None:
            self.contract_validity = m.get('contract_validity')
        if m.get('flow_desc') is not None:
            self.flow_desc = m.get('flow_desc')
        if m.get('flow_end_time') is not None:
            self.flow_end_time = m.get('flow_end_time')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('flow_start_time') is not None:
            self.flow_start_time = m.get('flow_start_time')
        if m.get('flow_status') is not None:
            self.flow_status = m.get('flow_status')
        if m.get('initiator_account_id') is not None:
            self.initiator_account_id = m.get('initiator_account_id')
        if m.get('initiator_authorized_account_id') is not None:
            self.initiator_authorized_account_id = m.get('initiator_authorized_account_id')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('sign_validity') is not None:
            self.sign_validity = m.get('sign_validity')
        return self


class CreateContractAccountsealimageRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        account_id: str = None,
        alias: str = None,
        height: int = None,
        width: int = None,
        type: str = None,
        data: str = None,
        transparent_flag: bool = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 用户id
        self.account_id = account_id
        # 印章别名
        self.alias = alias
        # 印章高度, 个人默认95px, 机构默认159px
        self.height = height
        # 印章宽度, 个人默认95px, 机构默认159px
        self.width = width
        # 印章数据类型，BASE64：base64格式
        self.type = type
        # 印章数据，base64格式字符串，不包含格式前缀
        self.data = data
        # 是否对图片进行透明化处理，默认false。仅对图片整体做透明化处理，无法去除图片背景
        self.transparent_flag = transparent_flag

    def validate(self):
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.type, 'type')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.account_id is not None:
            result['account_id'] = self.account_id
        if self.alias is not None:
            result['alias'] = self.alias
        if self.height is not None:
            result['height'] = self.height
        if self.width is not None:
            result['width'] = self.width
        if self.type is not None:
            result['type'] = self.type
        if self.data is not None:
            result['data'] = self.data
        if self.transparent_flag is not None:
            result['transparent_flag'] = self.transparent_flag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('account_id') is not None:
            self.account_id = m.get('account_id')
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('width') is not None:
            self.width = m.get('width')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('transparent_flag') is not None:
            self.transparent_flag = m.get('transparent_flag')
        return self


class CreateContractAccountsealimageResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        file_key: str = None,
        seal_id: str = None,
        url: str = None,
        height: int = None,
        width: int = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message
        # 印章fileKey
        self.file_key = file_key
        # 印章id
        self.seal_id = seal_id
        # 印章下载地址, 有效时间1小时
        self.url = url
        # 印章高度
        self.height = height
        # 印章宽度
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.file_key is not None:
            result['file_key'] = self.file_key
        if self.seal_id is not None:
            result['seal_id'] = self.seal_id
        if self.url is not None:
            result['url'] = self.url
        if self.height is not None:
            result['height'] = self.height
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('file_key') is not None:
            self.file_key = m.get('file_key')
        if m.get('seal_id') is not None:
            self.seal_id = m.get('seal_id')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class GetContractFileuploadurlRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        account_id: str = None,
        content_md_5: str = None,
        content_type: str = None,
        convert_2pdf: str = None,
        file_size: int = None,
        file_name: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 所属账号id，即个人账号id或机构账号id，如不传，则默认属于对接平台
        self.account_id = account_id
        # 先计算文件md5值，在对该md5值进行base64编码
        self.content_md_5 = content_md_5
        # 目标文件的MIME类型
        self.content_type = content_type
        # 是否转换成pdf文档，默认false，代表不做转换。转换是异步行为，如果指定要转换，需要调用查询文件信息接口查询状态，转换完成后才可使用。
        self.convert_2pdf = convert_2pdf
        # 文件大小，单位byte
        self.file_size = file_size
        # 文件名称（必须带上文件扩展名，不然会导致后续发起流程校验过不去 示例：合同.pdf ）
        self.file_name = file_name

    def validate(self):
        self.validate_required(self.content_md_5, 'content_md_5')
        self.validate_required(self.content_type, 'content_type')
        self.validate_required(self.convert_2pdf, 'convert_2pdf')
        self.validate_required(self.file_size, 'file_size')
        self.validate_required(self.file_name, 'file_name')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.account_id is not None:
            result['account_id'] = self.account_id
        if self.content_md_5 is not None:
            result['content_md5'] = self.content_md_5
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.convert_2pdf is not None:
            result['convert_2_pdf'] = self.convert_2pdf
        if self.file_size is not None:
            result['file_size'] = self.file_size
        if self.file_name is not None:
            result['file_name'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('account_id') is not None:
            self.account_id = m.get('account_id')
        if m.get('content_md5') is not None:
            self.content_md_5 = m.get('content_md5')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('convert_2_pdf') is not None:
            self.convert_2pdf = m.get('convert_2_pdf')
        if m.get('file_size') is not None:
            self.file_size = m.get('file_size')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        return self


class GetContractFileuploadurlResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        file_id: str = None,
        message: str = None,
        upload_url: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 文件Id
        self.file_id = file_id
        # 业务码信息
        self.message = message
        # 文件直传地址, 可以重复使用，但是只能传一样的文件，有效期一小时
        self.upload_url = upload_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.message is not None:
            result['message'] = self.message
        if self.upload_url is not None:
            result['upload_url'] = self.upload_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('upload_url') is not None:
            self.upload_url = m.get('upload_url')
        return self


class AddContractPlatformsignfieldsRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        flow_id: str = None,
        signfields: ContractPlatformSignFieldApplication = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 流程id
        self.flow_id = flow_id
        # 签署区列表数据
        self.signfields = signfields

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')
        self.validate_required(self.signfields, 'signfields')
        if self.signfields:
            self.signfields.validate()

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.signfields is not None:
            result['signfields'] = self.signfields.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('signfields') is not None:
            temp_model = ContractPlatformSignFieldApplication()
            self.signfields = temp_model.from_map(m['signfields'])
        return self


class AddContractPlatformsignfieldsResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        signfields: List[ContractSignField] = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message
        # 签署区列表数据
        self.signfields = signfields

    def validate(self):
        if self.signfields:
            for k in self.signfields:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        result['signfields'] = []
        if self.signfields is not None:
            for k in self.signfields:
                result['signfields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        self.signfields = []
        if m.get('signfields') is not None:
            for k in m.get('signfields'):
                temp_model = ContractSignField()
                self.signfields.append(temp_model.from_map(k))
        return self


class GetContractFileRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        file_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 文件id
        self.file_id = file_id

    def validate(self):
        self.validate_required(self.file_id, 'file_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class GetContractFileResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        file_id: str = None,
        name: str = None,
        download_url: str = None,
        size: int = None,
        status: int = None,
        pdf_total_pages: int = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message
        # 文件id
        self.file_id = file_id
        # 文件名称
        self.name = name
        # 下载地址
        self.download_url = download_url
        # 文件大小，单位byte
        self.size = size
        # 文件状态, 0:文件未上传；1:文件上传中 ；2：文件上传已完成,；3：文件上传失败 ；4：文件等待转pdf ；5：文件已转换pdf 。
        self.status = status
        # pdf文件总页数,仅当文件类型为pdf时有值
        self.pdf_total_pages = pdf_total_pages

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.name is not None:
            result['name'] = self.name
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.size is not None:
            result['size'] = self.size
        if self.status is not None:
            result['status'] = self.status
        if self.pdf_total_pages is not None:
            result['pdf_total_pages'] = self.pdf_total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('pdf_total_pages') is not None:
            self.pdf_total_pages = m.get('pdf_total_pages')
        return self


class QueryContractAccountsealsRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        account_id: str = None,
        offset: int = None,
        size: int = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 用户id
        self.account_id = account_id
        # 分页起始位置
        self.offset = offset
        # 单页数量
        self.size = size

    def validate(self):
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.offset, 'offset')
        self.validate_required(self.size, 'size')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.account_id is not None:
            result['account_id'] = self.account_id
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('account_id') is not None:
            self.account_id = m.get('account_id')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class QueryContractAccountsealsResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        total: int = None,
        seals: List[ContractSeal] = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message
        # 查询总数
        self.total = total
        # 印章列表
        self.seals = seals

    def validate(self):
        if self.seals:
            for k in self.seals:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.total is not None:
            result['total'] = self.total
        result['seals'] = []
        if self.seals is not None:
            for k in self.seals:
                result['seals'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('total') is not None:
            self.total = m.get('total')
        self.seals = []
        if m.get('seals') is not None:
            for k in m.get('seals'):
                temp_model = ContractSeal()
                self.seals.append(temp_model.from_map(k))
        return self


class QueryContractOrganizationsealsRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        org_id: str = None,
        offset: int = None,
        size: int = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 机构id
        self.org_id = org_id
        # 分页起始位置
        self.offset = offset
        # 单页数量
        self.size = size

    def validate(self):
        self.validate_required(self.org_id, 'org_id')
        self.validate_required(self.offset, 'offset')
        self.validate_required(self.size, 'size')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.org_id is not None:
            result['org_id'] = self.org_id
        if self.offset is not None:
            result['offset'] = self.offset
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('org_id') is not None:
            self.org_id = m.get('org_id')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class QueryContractOrganizationsealsResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        total: int = None,
        seals: List[ContractSeal] = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message
        # 查询总数
        self.total = total
        # 印章列表
        self.seals = seals

    def validate(self):
        if self.seals:
            for k in self.seals:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.total is not None:
            result['total'] = self.total
        result['seals'] = []
        if self.seals is not None:
            for k in self.seals:
                result['seals'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('total') is not None:
            self.total = m.get('total')
        self.seals = []
        if m.get('seals') is not None:
            for k in m.get('seals'):
                temp_model = ContractSeal()
                self.seals.append(temp_model.from_map(k))
        return self


class QueryContractFlowsignerRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        flow_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 流程id
        self.flow_id = flow_id

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        return self


class QueryContractFlowsignerResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        signers: List[ContractFlowSigner] = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message
        # 签字人列表
        self.signers = signers

    def validate(self):
        if self.signers:
            for k in self.signers:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        result['signers'] = []
        if self.signers is not None:
            for k in self.signers:
                result['signers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        self.signers = []
        if m.get('signers') is not None:
            for k in m.get('signers'):
                temp_model = ContractFlowSigner()
                self.signers.append(temp_model.from_map(k))
        return self


class QueryContractSignfieldsRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        flow_id: str = None,
        account_id: str = None,
        signfield_ids: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 流程id
        self.flow_id = flow_id
        # 账号id，默认所有签署人
        self.account_id = account_id
        # 指定签署区id列表，逗号分割，默认所有签署区
        self.signfield_ids = signfield_ids

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.account_id is not None:
            result['account_id'] = self.account_id
        if self.signfield_ids is not None:
            result['signfield_ids'] = self.signfield_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('account_id') is not None:
            self.account_id = m.get('account_id')
        if m.get('signfield_ids') is not None:
            self.signfield_ids = m.get('signfield_ids')
        return self


class QueryContractSignfieldsResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        signfields: List[ContractSignFieldDetail] = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message
        # 签署区列表数据
        self.signfields = signfields

    def validate(self):
        if self.signfields:
            for k in self.signfields:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        result['signfields'] = []
        if self.signfields is not None:
            for k in self.signfields:
                result['signfields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        self.signfields = []
        if m.get('signfields') is not None:
            for k in m.get('signfields'):
                temp_model = ContractSignFieldDetail()
                self.signfields.append(temp_model.from_map(k))
        return self


class QueryContractAccountRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        account_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 个人账号id
        self.account_id = account_id

    def validate(self):
        self.validate_required(self.account_id, 'account_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.account_id is not None:
            result['account_id'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('account_id') is not None:
            self.account_id = m.get('account_id')
        return self


class QueryContractAccountResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        account_id: str = None,
        name: str = None,
        id_type: str = None,
        id_number: str = None,
        mobile: str = None,
        email: str = None,
        third_party_user_id: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message
        # 个人账号id
        self.account_id = account_id
        # 姓名
        self.name = name
        # 证件类型，详见个人证件类型说明
        self.id_type = id_type
        # 证件号
        self.id_number = id_number
        # 联系方式，手机号码
        self.mobile = mobile
        # 联系方式，邮箱地址
        self.email = email
        # 第三方平台的用户id
        self.third_party_user_id = third_party_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.account_id is not None:
            result['account_id'] = self.account_id
        if self.name is not None:
            result['name'] = self.name
        if self.id_type is not None:
            result['id_type'] = self.id_type
        if self.id_number is not None:
            result['id_number'] = self.id_number
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.email is not None:
            result['email'] = self.email
        if self.third_party_user_id is not None:
            result['third_party_user_id'] = self.third_party_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('account_id') is not None:
            self.account_id = m.get('account_id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id_type') is not None:
            self.id_type = m.get('id_type')
        if m.get('id_number') is not None:
            self.id_number = m.get('id_number')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('third_party_user_id') is not None:
            self.third_party_user_id = m.get('third_party_user_id')
        return self


class QueryContractOrganizationRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        org_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 机构账号id
        self.org_id = org_id

    def validate(self):
        self.validate_required(self.org_id, 'org_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.org_id is not None:
            result['org_id'] = self.org_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('org_id') is not None:
            self.org_id = m.get('org_id')
        return self


class QueryContractOrganizationResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        org_id: str = None,
        name: str = None,
        id_type: str = None,
        id_number: str = None,
        org_legal_id_number: str = None,
        org_legal_name: str = None,
        third_party_user_id: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message
        # 机构账号Id
        self.org_id = org_id
        # 机构名称
        self.name = name
        # 证件类型，详见机构证件类型说明
        self.id_type = id_type
        # 证件号
        self.id_number = id_number
        # 企业法人证件号
        self.org_legal_id_number = org_legal_id_number
        # 企业法人名称
        self.org_legal_name = org_legal_name
        # 第三方平台的机构id
        self.third_party_user_id = third_party_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.org_id is not None:
            result['org_id'] = self.org_id
        if self.name is not None:
            result['name'] = self.name
        if self.id_type is not None:
            result['id_type'] = self.id_type
        if self.id_number is not None:
            result['id_number'] = self.id_number
        if self.org_legal_id_number is not None:
            result['org_legal_id_number'] = self.org_legal_id_number
        if self.org_legal_name is not None:
            result['org_legal_name'] = self.org_legal_name
        if self.third_party_user_id is not None:
            result['third_party_user_id'] = self.third_party_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('org_id') is not None:
            self.org_id = m.get('org_id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id_type') is not None:
            self.id_type = m.get('id_type')
        if m.get('id_number') is not None:
            self.id_number = m.get('id_number')
        if m.get('org_legal_id_number') is not None:
            self.org_legal_id_number = m.get('org_legal_id_number')
        if m.get('org_legal_name') is not None:
            self.org_legal_name = m.get('org_legal_name')
        if m.get('third_party_user_id') is not None:
            self.third_party_user_id = m.get('third_party_user_id')
        return self


class QueryContractTemplateRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        template_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 模板id
        self.template_id = template_id

    def validate(self):
        self.validate_required(self.template_id, 'template_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.template_id is not None:
            result['template_id'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')
        return self


class QueryContractTemplateResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        create_time: int = None,
        download_url: str = None,
        file_size: int = None,
        message: str = None,
        struct_components: List[ContractTemplateStructComponent] = None,
        template_id: str = None,
        template_name: str = None,
        update_time: int = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 创建时间
        self.create_time = create_time
        # 模板文件下载地址
        self.download_url = download_url
        # 模板文件大小
        self.file_size = file_size
        # 业务码信息
        self.message = message
        # 文件模板中的输入项组件列表
        self.struct_components = struct_components
        # 模板id
        self.template_id = template_id
        # 模板名称
        self.template_name = template_name
        # 更新时间
        self.update_time = update_time

    def validate(self):
        if self.struct_components:
            for k in self.struct_components:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.create_time is not None:
            result['create_time'] = self.create_time
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.file_size is not None:
            result['file_size'] = self.file_size
        if self.message is not None:
            result['message'] = self.message
        result['struct_components'] = []
        if self.struct_components is not None:
            for k in self.struct_components:
                result['struct_components'].append(k.to_map() if k else None)
        if self.template_id is not None:
            result['template_id'] = self.template_id
        if self.template_name is not None:
            result['template_name'] = self.template_name
        if self.update_time is not None:
            result['update_time'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('create_time') is not None:
            self.create_time = m.get('create_time')
        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')
        if m.get('file_size') is not None:
            self.file_size = m.get('file_size')
        if m.get('message') is not None:
            self.message = m.get('message')
        self.struct_components = []
        if m.get('struct_components') is not None:
            for k in m.get('struct_components'):
                temp_model = ContractTemplateStructComponent()
                self.struct_components.append(temp_model.from_map(k))
        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')
        if m.get('template_name') is not None:
            self.template_name = m.get('template_name')
        if m.get('update_time') is not None:
            self.update_time = m.get('update_time')
        return self


class CreateContractSignflowRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        auto_archive: bool = None,
        auto_deduction_force: bool = None,
        business_scene: str = None,
        contract_sign_flow_config: ContractSignFlowConfig = None,
        initiator_account_id: str = None,
        initiator_authorized_account_id: str = None,
        repayment_order_info: List[RepaymentOrderRequest] = None,
        sign_platform: str = None,
        sign_validity: int = None,
        payer_tuid: str = None,
        payee_tuid: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 是否自动归档，默认false 如设置为true，则在流程开启后，当所有签署人签署完毕，系统自动将流程归档，状态变为“已完成”状态，在流程状态为“已完成”前，可随时添加签署人；如设置为false，则在调用流程开启后，需主动调用签署流程归档接口，将流程状态变更为“已完成”，归档前可随时添加签署人；已完成的流程才可下载签署后的文件
        self.auto_archive = auto_archive
        # 是否强制代扣
        self.auto_deduction_force = auto_deduction_force
        # 文件主题
        self.business_scene = business_scene
        # 任务配置信息
        self.contract_sign_flow_config = contract_sign_flow_config
        # 发起人账户id，即发起本次签署的操作人个人账号id；如不传，默认由对接平台发起
        self.initiator_account_id = initiator_account_id
        # 发起方主体id，如存在个人代机构发起签约，则需传入机构id；如不传，则默认是对接平台
        self.initiator_authorized_account_id = initiator_authorized_account_id
        # 代扣规则详情
        self.repayment_order_info = repayment_order_info
        # 签署平台，ALIPAY（支付宝小程序）或H5
        self.sign_platform = sign_platform
        # 签署有效截止日期，毫秒，默认3天失效
        self.sign_validity = sign_validity
        # 付款方ID（个人）
        self.payer_tuid = payer_tuid
        # 收款方ID(机构)
        self.payee_tuid = payee_tuid

    def validate(self):
        self.validate_required(self.business_scene, 'business_scene')
        if self.contract_sign_flow_config:
            self.contract_sign_flow_config.validate()
        if self.repayment_order_info:
            for k in self.repayment_order_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.auto_archive is not None:
            result['auto_archive'] = self.auto_archive
        if self.auto_deduction_force is not None:
            result['auto_deduction_force'] = self.auto_deduction_force
        if self.business_scene is not None:
            result['business_scene'] = self.business_scene
        if self.contract_sign_flow_config is not None:
            result['contract_sign_flow_config'] = self.contract_sign_flow_config.to_map()
        if self.initiator_account_id is not None:
            result['initiator_account_id'] = self.initiator_account_id
        if self.initiator_authorized_account_id is not None:
            result['initiator_authorized_account_id'] = self.initiator_authorized_account_id
        result['repayment_order_info'] = []
        if self.repayment_order_info is not None:
            for k in self.repayment_order_info:
                result['repayment_order_info'].append(k.to_map() if k else None)
        if self.sign_platform is not None:
            result['sign_platform'] = self.sign_platform
        if self.sign_validity is not None:
            result['sign_validity'] = self.sign_validity
        if self.payer_tuid is not None:
            result['payer_tuid'] = self.payer_tuid
        if self.payee_tuid is not None:
            result['payee_tuid'] = self.payee_tuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('auto_archive') is not None:
            self.auto_archive = m.get('auto_archive')
        if m.get('auto_deduction_force') is not None:
            self.auto_deduction_force = m.get('auto_deduction_force')
        if m.get('business_scene') is not None:
            self.business_scene = m.get('business_scene')
        if m.get('contract_sign_flow_config') is not None:
            temp_model = ContractSignFlowConfig()
            self.contract_sign_flow_config = temp_model.from_map(m['contract_sign_flow_config'])
        if m.get('initiator_account_id') is not None:
            self.initiator_account_id = m.get('initiator_account_id')
        if m.get('initiator_authorized_account_id') is not None:
            self.initiator_authorized_account_id = m.get('initiator_authorized_account_id')
        self.repayment_order_info = []
        if m.get('repayment_order_info') is not None:
            for k in m.get('repayment_order_info'):
                temp_model = RepaymentOrderRequest()
                self.repayment_order_info.append(temp_model.from_map(k))
        if m.get('sign_platform') is not None:
            self.sign_platform = m.get('sign_platform')
        if m.get('sign_validity') is not None:
            self.sign_validity = m.get('sign_validity')
        if m.get('payer_tuid') is not None:
            self.payer_tuid = m.get('payer_tuid')
        if m.get('payee_tuid') is not None:
            self.payee_tuid = m.get('payee_tuid')
        return self


class CreateContractSignflowResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        flow_id: str = None,
        message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 签约流程ID
        self.flow_id = flow_id
        # 业务码信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateContractRegisterzftRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        address: str = None,
        agent_account_id: str = None,
        alias_name: str = None,
        alipay_logon_id: str = None,
        apply_time: str = None,
        binding_alipay_logon_id: str = None,
        card_alias_no: str = None,
        cert_image: str = None,
        cert_no: str = None,
        cert_type: str = None,
        city_code: str = None,
        contact_email: str = None,
        contact_mobile: str = None,
        contact_name: str = None,
        contact_phone: str = None,
        contact_tag: str = None,
        contact_type: str = None,
        district_code: str = None,
        ext_info: str = None,
        ip_role_id: str = None,
        legal_cert_back_image: str = None,
        legal_cert_front_image: str = None,
        legal_cert_no: str = None,
        legal_name: str = None,
        mcc: str = None,
        merchant_name: str = None,
        merchant_type: str = None,
        name: str = None,
        order_id: str = None,
        out_biz_no: str = None,
        out_door_image: str = None,
        platform_tuid: str = None,
        province_code: str = None,
        service: str = None,
        service_phone: str = None,
        sign_time_with_isv: str = None,
        site_name: str = None,
        site_type: str = None,
        site_url: str = None,
        smid: str = None,
        status: str = None,
        update: int = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 地址。商户详细经营地址或人员所在地点
        self.address = address
        # 代理商户的账户
        self.agent_account_id = agent_account_id
        # 商户别名
        self.alias_name = alias_name
        # 商户支付宝账户
        self.alipay_logon_id = alipay_logon_id
        # 申请时间
        self.apply_time = apply_time
        # 二级商户支付宝账户，用于协议确认。目前商业场景（除医疗、中小学教育等）下必填。本字段要求与商户名称name同名，且是实名认证支付宝账户
        self.binding_alipay_logon_id = binding_alipay_logon_id
        # 结算卡id
        self.card_alias_no = card_alias_no
        # 营业执照图片url，本业务接口中，如果是特殊行业必填。其值为使用ant.merchant.expand.indirect.image.upload上传图片得到的一串oss key。
        self.cert_image = cert_image
        # 商户社会信用码
        self.cert_no = cert_no
        # 商户证件类型，取值范围：201：营业执照；2011:营业执照(统一社会信用代码)；204：民办非企业登记证书；206：社会团体法人登记证书；218：事业单位法人证书；219：党政机关批准设立文件/行政执法主体资格证；100：个人商户身份证
        self.cert_type = cert_type
        # 城市编码。请按照https://gw.alipayobjects.com/os/basement_prod/253c4dcb-b8a4-4a1e-8be2-79e191a9b6db.xlsx 表格中内容填写。
        # （参考资料：
        # http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/）
        self.city_code = city_code
        # 电子邮箱
        self.contact_email = contact_email
        # 商户联系人信息
        self.contact_mobile = contact_mobile
        # 联系人名字
        self.contact_name = contact_name
        # 商户联系人电话信息
        self.contact_phone = contact_phone
        # 商户联系人业务标识枚举，表示商户联系人的职责。异议处理接口人:02;商户关键联系人:06;数据反馈接口人:11;服务联动接口人:08
        self.contact_tag = contact_tag
        # 联系人类型，取值范围：LEGAL_PERSON：法人；CONTROLLER：实际控制人；AGENT：代理人；OTHER：其他
        self.contact_type = contact_type
        # 区县编码。请按照https://gw.alipayobjects.com/os/basement_prod/253c4dcb-b8a4-4a1e-8be2-79e191a9b6db.xlsx 表格中内容填写。
        # （参考资料：
        # http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/）
        self.district_code = district_code
        # 返回申请单相关参数。当前返回内容有cardAliasNo，smid
        self.ext_info = ext_info
        # 商户角色id。审核通过后生成。间连商户或平台商二级商户业务中，本字段表示smid
        self.ip_role_id = ip_role_id
        # 法人身份证反面url，其值为使用ant.merchant.expand.indirect.image.upload上传图片得到的一串oss key。本业务接口中，如果是特殊行业必填
        self.legal_cert_back_image = legal_cert_back_image
        # 法人身份证正面url，其值为使用ant.merchant.expand.indirect.image.upload上传图片得到的一串oss key。本业务接口中，如果是特殊行业必填
        self.legal_cert_front_image = legal_cert_front_image
        # 法人身份证号
        self.legal_cert_no = legal_cert_no
        # 法人名称
        self.legal_name = legal_name
        # 商户类别码mcc，参见附件描述中的“类目code” https://gw.alipayobjects.com/os/basement_prod/82cb70f7-abbd-417a-91ba-73c1849f07ea.xlsx 如果要求资质一栏不为空，表明是特殊行业，会有人工审核。注：文档更新可能有滞后性，以实际为准
        self.mcc = mcc
        # 蚂蚁金服（杭*****术有限公司
        self.merchant_name = merchant_name
        # 商家类型：01：企业；02：事业单位；03：民办非企业组织；04：社会团体；05：党政及国家机关；06：个人商户；07：个体工商户
        self.merchant_type = merchant_type
        # 商户名称
        self.name = name
        # 申请单id
        self.order_id = order_id
        # 外部业务号。比如某种业务标准外部订单号,比如交易外部订单号，代表服务商端自己订单号。用于做并发控制，防止一笔外部订单发起两次进件。非必要场景禁止传入本字段，如要使用务必理清场景及字段生成规则，与蚂蚁金服对接人咨询。
        self.out_biz_no = out_biz_no
        # 门头照，其值为使用ant.merchant.expand.indirect.image.upload上传图片得到的一串oss key。如果使用当面付服务则必填
        self.out_door_image = out_door_image
        # 商户在智能合同平台唯一id
        self.platform_tuid = platform_tuid
        # 省份编码。请按照https://gw.alipayobjects.com/os/basement_prod/253c4dcb-b8a4-4a1e-8be2-79e191a9b6db.xlsx 表格中内容填写。
        # （参考资料：
        # http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/）
        self.province_code = province_code
        # 商户使用服务，可选值有：当面付、app支付、wap支付、电脑支付
        self.service = service
        # 客服电话
        self.service_phone = service_phone
        # 二级商户与服务商的签约时间
        self.sign_time_with_isv = sign_time_with_isv
        # 站点名称
        self.site_name = site_name
        # 网站：01
        # APP : 02
        # 服务窗:03
        # 公众号:04
        # 其他:05
        # 支付宝小程序:06
        self.site_type = site_type
        # 站点地址
        self.site_url = site_url
        # 二级商户id
        self.smid = smid
        # 申请单状态。99:已完结;-1:失败;031:已提交审核
        self.status = status
        # 0表示不更新，1表示强制更新
        self.update = update

    def validate(self):
        self.validate_required(self.address, 'address')
        self.validate_required(self.alias_name, 'alias_name')
        self.validate_required(self.alipay_logon_id, 'alipay_logon_id')
        self.validate_required(self.apply_time, 'apply_time')
        if self.apply_time is not None:
            self.validate_pattern(self.apply_time, 'apply_time', '\\d{4}[-]\\d{1,2}[-]\\d{1,2}[T]\\d{2}:\\d{2}:\\d{2}([Z]|([\\.]\\d{1,9})?[\\+]\\d{2}[\\:]?\\d{2})')
        self.validate_required(self.binding_alipay_logon_id, 'binding_alipay_logon_id')
        self.validate_required(self.cert_image, 'cert_image')
        self.validate_required(self.cert_no, 'cert_no')
        self.validate_required(self.cert_type, 'cert_type')
        self.validate_required(self.city_code, 'city_code')
        self.validate_required(self.contact_email, 'contact_email')
        self.validate_required(self.contact_mobile, 'contact_mobile')
        self.validate_required(self.contact_name, 'contact_name')
        self.validate_required(self.contact_phone, 'contact_phone')
        self.validate_required(self.contact_tag, 'contact_tag')
        self.validate_required(self.contact_type, 'contact_type')
        self.validate_required(self.district_code, 'district_code')
        self.validate_required(self.ext_info, 'ext_info')
        self.validate_required(self.ip_role_id, 'ip_role_id')
        self.validate_required(self.legal_cert_back_image, 'legal_cert_back_image')
        self.validate_required(self.legal_cert_front_image, 'legal_cert_front_image')
        self.validate_required(self.legal_cert_no, 'legal_cert_no')
        self.validate_required(self.legal_name, 'legal_name')
        self.validate_required(self.mcc, 'mcc')
        self.validate_required(self.merchant_name, 'merchant_name')
        self.validate_required(self.merchant_type, 'merchant_type')
        self.validate_required(self.name, 'name')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.out_biz_no, 'out_biz_no')
        self.validate_required(self.out_door_image, 'out_door_image')
        self.validate_required(self.platform_tuid, 'platform_tuid')
        self.validate_required(self.province_code, 'province_code')
        self.validate_required(self.service, 'service')
        self.validate_required(self.service_phone, 'service_phone')
        self.validate_required(self.sign_time_with_isv, 'sign_time_with_isv')
        self.validate_required(self.site_name, 'site_name')
        self.validate_required(self.site_type, 'site_type')
        self.validate_required(self.site_url, 'site_url')
        self.validate_required(self.smid, 'smid')
        self.validate_required(self.status, 'status')
        self.validate_required(self.update, 'update')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.address is not None:
            result['address'] = self.address
        if self.agent_account_id is not None:
            result['agent_account_id'] = self.agent_account_id
        if self.alias_name is not None:
            result['alias_name'] = self.alias_name
        if self.alipay_logon_id is not None:
            result['alipay_logon_id'] = self.alipay_logon_id
        if self.apply_time is not None:
            result['apply_time'] = self.apply_time
        if self.binding_alipay_logon_id is not None:
            result['binding_alipay_logon_id'] = self.binding_alipay_logon_id
        if self.card_alias_no is not None:
            result['card_alias_no'] = self.card_alias_no
        if self.cert_image is not None:
            result['cert_image'] = self.cert_image
        if self.cert_no is not None:
            result['cert_no'] = self.cert_no
        if self.cert_type is not None:
            result['cert_type'] = self.cert_type
        if self.city_code is not None:
            result['city_code'] = self.city_code
        if self.contact_email is not None:
            result['contact_email'] = self.contact_email
        if self.contact_mobile is not None:
            result['contact_mobile'] = self.contact_mobile
        if self.contact_name is not None:
            result['contact_name'] = self.contact_name
        if self.contact_phone is not None:
            result['contact_phone'] = self.contact_phone
        if self.contact_tag is not None:
            result['contact_tag'] = self.contact_tag
        if self.contact_type is not None:
            result['contact_type'] = self.contact_type
        if self.district_code is not None:
            result['district_code'] = self.district_code
        if self.ext_info is not None:
            result['ext_info'] = self.ext_info
        if self.ip_role_id is not None:
            result['ip_role_id'] = self.ip_role_id
        if self.legal_cert_back_image is not None:
            result['legal_cert_back_image'] = self.legal_cert_back_image
        if self.legal_cert_front_image is not None:
            result['legal_cert_front_image'] = self.legal_cert_front_image
        if self.legal_cert_no is not None:
            result['legal_cert_no'] = self.legal_cert_no
        if self.legal_name is not None:
            result['legal_name'] = self.legal_name
        if self.mcc is not None:
            result['mcc'] = self.mcc
        if self.merchant_name is not None:
            result['merchant_name'] = self.merchant_name
        if self.merchant_type is not None:
            result['merchant_type'] = self.merchant_type
        if self.name is not None:
            result['name'] = self.name
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.out_biz_no is not None:
            result['out_biz_no'] = self.out_biz_no
        if self.out_door_image is not None:
            result['out_door_image'] = self.out_door_image
        if self.platform_tuid is not None:
            result['platform_tuid'] = self.platform_tuid
        if self.province_code is not None:
            result['province_code'] = self.province_code
        if self.service is not None:
            result['service'] = self.service
        if self.service_phone is not None:
            result['service_phone'] = self.service_phone
        if self.sign_time_with_isv is not None:
            result['sign_time_with_isv'] = self.sign_time_with_isv
        if self.site_name is not None:
            result['site_name'] = self.site_name
        if self.site_type is not None:
            result['site_type'] = self.site_type
        if self.site_url is not None:
            result['site_url'] = self.site_url
        if self.smid is not None:
            result['smid'] = self.smid
        if self.status is not None:
            result['status'] = self.status
        if self.update is not None:
            result['update'] = self.update
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('agent_account_id') is not None:
            self.agent_account_id = m.get('agent_account_id')
        if m.get('alias_name') is not None:
            self.alias_name = m.get('alias_name')
        if m.get('alipay_logon_id') is not None:
            self.alipay_logon_id = m.get('alipay_logon_id')
        if m.get('apply_time') is not None:
            self.apply_time = m.get('apply_time')
        if m.get('binding_alipay_logon_id') is not None:
            self.binding_alipay_logon_id = m.get('binding_alipay_logon_id')
        if m.get('card_alias_no') is not None:
            self.card_alias_no = m.get('card_alias_no')
        if m.get('cert_image') is not None:
            self.cert_image = m.get('cert_image')
        if m.get('cert_no') is not None:
            self.cert_no = m.get('cert_no')
        if m.get('cert_type') is not None:
            self.cert_type = m.get('cert_type')
        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')
        if m.get('contact_email') is not None:
            self.contact_email = m.get('contact_email')
        if m.get('contact_mobile') is not None:
            self.contact_mobile = m.get('contact_mobile')
        if m.get('contact_name') is not None:
            self.contact_name = m.get('contact_name')
        if m.get('contact_phone') is not None:
            self.contact_phone = m.get('contact_phone')
        if m.get('contact_tag') is not None:
            self.contact_tag = m.get('contact_tag')
        if m.get('contact_type') is not None:
            self.contact_type = m.get('contact_type')
        if m.get('district_code') is not None:
            self.district_code = m.get('district_code')
        if m.get('ext_info') is not None:
            self.ext_info = m.get('ext_info')
        if m.get('ip_role_id') is not None:
            self.ip_role_id = m.get('ip_role_id')
        if m.get('legal_cert_back_image') is not None:
            self.legal_cert_back_image = m.get('legal_cert_back_image')
        if m.get('legal_cert_front_image') is not None:
            self.legal_cert_front_image = m.get('legal_cert_front_image')
        if m.get('legal_cert_no') is not None:
            self.legal_cert_no = m.get('legal_cert_no')
        if m.get('legal_name') is not None:
            self.legal_name = m.get('legal_name')
        if m.get('mcc') is not None:
            self.mcc = m.get('mcc')
        if m.get('merchant_name') is not None:
            self.merchant_name = m.get('merchant_name')
        if m.get('merchant_type') is not None:
            self.merchant_type = m.get('merchant_type')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('out_biz_no') is not None:
            self.out_biz_no = m.get('out_biz_no')
        if m.get('out_door_image') is not None:
            self.out_door_image = m.get('out_door_image')
        if m.get('platform_tuid') is not None:
            self.platform_tuid = m.get('platform_tuid')
        if m.get('province_code') is not None:
            self.province_code = m.get('province_code')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('service_phone') is not None:
            self.service_phone = m.get('service_phone')
        if m.get('sign_time_with_isv') is not None:
            self.sign_time_with_isv = m.get('sign_time_with_isv')
        if m.get('site_name') is not None:
            self.site_name = m.get('site_name')
        if m.get('site_type') is not None:
            self.site_type = m.get('site_type')
        if m.get('site_url') is not None:
            self.site_url = m.get('site_url')
        if m.get('smid') is not None:
            self.smid = m.get('smid')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('update') is not None:
            self.update = m.get('update')
        return self


class CreateContractRegisterzftResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 错误码
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class CreateContractPlatformtemplateRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        auto_deduction: bool = None,
        content_md_5: str = None,
        content_type: str = None,
        convert_2pdf: bool = None,
        file_name: str = None,
        sign_fields: List[ContractPlatformSignField] = None,
        user_sign_pages: List[int] = None,
        auto_deduction_force: bool = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 是否包含代扣规则，如果设置为true，则在创建手动签署流程时，必须传入代扣规则。默认为false
        self.auto_deduction = auto_deduction
        # Base64编码的模板文件的MD5值
        self.content_md_5 = content_md_5
        # 目标文件的MIME类型
        self.content_type = content_type
        # 是否需要转成pdf，如果模板文件为.doc/.docx 传true，为pdf传false
        self.convert_2pdf = convert_2pdf
        # 文件名称，必须带扩展名如:.pdf,.doc,.docx
        self.file_name = file_name
        # 平台方的签署信息列表
        self.sign_fields = sign_fields
        # 用户需要签章的页面列表（默认为最后一页）
        self.user_sign_pages = user_sign_pages
        # 是否强制用户选择代扣
        self.auto_deduction_force = auto_deduction_force

    def validate(self):
        self.validate_required(self.content_md_5, 'content_md_5')
        self.validate_required(self.content_type, 'content_type')
        self.validate_required(self.convert_2pdf, 'convert_2pdf')
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.sign_fields, 'sign_fields')
        if self.sign_fields:
            for k in self.sign_fields:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.auto_deduction is not None:
            result['auto_deduction'] = self.auto_deduction
        if self.content_md_5 is not None:
            result['content_md5'] = self.content_md_5
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.convert_2pdf is not None:
            result['convert2_pdf'] = self.convert_2pdf
        if self.file_name is not None:
            result['file_name'] = self.file_name
        result['sign_fields'] = []
        if self.sign_fields is not None:
            for k in self.sign_fields:
                result['sign_fields'].append(k.to_map() if k else None)
        if self.user_sign_pages is not None:
            result['user_sign_pages'] = self.user_sign_pages
        if self.auto_deduction_force is not None:
            result['auto_deduction_force'] = self.auto_deduction_force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('auto_deduction') is not None:
            self.auto_deduction = m.get('auto_deduction')
        if m.get('content_md5') is not None:
            self.content_md_5 = m.get('content_md5')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('convert2_pdf') is not None:
            self.convert_2pdf = m.get('convert2_pdf')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        self.sign_fields = []
        if m.get('sign_fields') is not None:
            for k in m.get('sign_fields'):
                temp_model = ContractPlatformSignField()
                self.sign_fields.append(temp_model.from_map(k))
        if m.get('user_sign_pages') is not None:
            self.user_sign_pages = m.get('user_sign_pages')
        if m.get('auto_deduction_force') is not None:
            self.auto_deduction_force = m.get('auto_deduction_force')
        return self


class CreateContractPlatformtemplateResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        template_id: str = None,
        upload_url: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message
        # 模板ID
        self.template_id = template_id
        # 文件直传地址，需要用此上传地址使用put方式上传文件，只有文件上传后模板才可用
        self.upload_url = upload_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.template_id is not None:
            result['template_id'] = self.template_id
        if self.upload_url is not None:
            result['upload_url'] = self.upload_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')
        if m.get('upload_url') is not None:
            self.upload_url = m.get('upload_url')
        return self


class QueryContractMerchantzftRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        agent_account_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 代理商户账户
        self.agent_account_id = agent_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.agent_account_id is not None:
            result['agent_account_id'] = self.agent_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('agent_account_id') is not None:
            self.agent_account_id = m.get('agent_account_id')
        return self


class QueryContractMerchantzftResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        data: str = None,
        err_message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 0表示成功，其他为失败
        self.code = code
        # 商户入驻查询信息
        self.data = data
        # 错误信息描述
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.err_message is not None:
            result['err_message'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        return self


class ListContractOuttradeidRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        flow_id: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 合同id
        self.flow_id = flow_id
        # 分页第几页
        self.page_index = page_index
        # 每页的大小
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')
        self.validate_required(self.page_index, 'page_index')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.page_index is not None:
            result['page_index'] = self.page_index
        if self.page_size is not None:
            result['page_size'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('page_index') is not None:
            self.page_index = m.get('page_index')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        return self


class ListContractOuttradeidResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        total: int = None,
        out_trade_no: List[str] = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 错误码
        self.code = code
        # 错误信息描述
        self.err_message = err_message
        # 总符合条件的交易个数
        self.total = total
        # 所有符合条件交易相关的id
        self.out_trade_no = out_trade_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.total is not None:
            result['total'] = self.total
        if self.out_trade_no is not None:
            result['out_trade_no'] = self.out_trade_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('out_trade_no') is not None:
            self.out_trade_no = m.get('out_trade_no')
        return self


class QueryContractTradedetailRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        flow_id: str = None,
        out_trade_no: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 合同id
        self.flow_id = flow_id
        # out_trade_no
        self.out_trade_no = out_trade_no

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')
        self.validate_required(self.out_trade_no, 'out_trade_no')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.out_trade_no is not None:
            result['out_trade_no'] = self.out_trade_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('out_trade_no') is not None:
            self.out_trade_no = m.get('out_trade_no')
        return self


class QueryContractTradedetailResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        data: str = None,
        err_message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 错误码
        self.code = code
        # 订单详情
        self.data = data
        # 错误信息描述
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.err_message is not None:
            result['err_message'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        return self


class CreateContractMerchantrefundRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        flow_id: str = None,
        out_request_no: str = None,
        out_trade_no: str = None,
        refund_amount: int = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 合同id
        self.flow_id = flow_id
        # 退款请求对应的码
        self.out_request_no = out_request_no
        # 订单id
        self.out_trade_no = out_trade_no
        # 退款金额
        self.refund_amount = refund_amount

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')
        self.validate_required(self.out_request_no, 'out_request_no')
        self.validate_required(self.out_trade_no, 'out_trade_no')
        self.validate_required(self.refund_amount, 'refund_amount')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.out_request_no is not None:
            result['out_request_no'] = self.out_request_no
        if self.out_trade_no is not None:
            result['out_trade_no'] = self.out_trade_no
        if self.refund_amount is not None:
            result['refund_amount'] = self.refund_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('out_request_no') is not None:
            self.out_request_no = m.get('out_request_no')
        if m.get('out_trade_no') is not None:
            self.out_trade_no = m.get('out_trade_no')
        if m.get('refund_amount') is not None:
            self.refund_amount = m.get('refund_amount')
        return self


class CreateContractMerchantrefundResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        out_request_no: str = None,
        out_trade_no: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 错误码
        self.code = code
        # 错误信息描述
        self.message = message
        # 本次请求对应的操作单号
        self.out_request_no = out_request_no
        # 订单id
        self.out_trade_no = out_trade_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.out_request_no is not None:
            result['out_request_no'] = self.out_request_no
        if self.out_trade_no is not None:
            result['out_trade_no'] = self.out_trade_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('out_request_no') is not None:
            self.out_request_no = m.get('out_request_no')
        if m.get('out_trade_no') is not None:
            self.out_trade_no = m.get('out_trade_no')
        return self


class CreateContractAdminaccountRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        return self


class CreateContractAdminaccountResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 错误码
        self.code = code
        # 错误信息描述
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        return self


class ListContractTradeidsRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        flow_id: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 合同id
        self.flow_id = flow_id
        # 1
        self.page_index = page_index
        # 页面大小
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')
        self.validate_required(self.page_index, 'page_index')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.page_index is not None:
            result['page_index'] = self.page_index
        if self.page_size is not None:
            result['page_size'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('page_index') is not None:
            self.page_index = m.get('page_index')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        return self


class ListContractTradeidsResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        total: int = None,
        out_trade_no: List[str] = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 0表示成功
        self.code = code
        # 错误信息描述
        self.err_message = err_message
        # 所有item的个数
        self.total = total
        # 所有满足条件的订单
        self.out_trade_no = out_trade_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.total is not None:
            result['total'] = self.total
        if self.out_trade_no is not None:
            result['out_trade_no'] = self.out_trade_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('out_trade_no') is not None:
            self.out_trade_no = m.get('out_trade_no')
        return self


class CreateContractCommontriggerRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        repayment_order_info: List[RepaymentOrderRequest] = None,
        flow_id: str = None,
        user_tuid: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 代扣规则详情
        self.repayment_order_info = repayment_order_info
        # 合同id
        self.flow_id = flow_id
        # 用户在智能合同平台的身份
        self.user_tuid = user_tuid

    def validate(self):
        self.validate_required(self.repayment_order_info, 'repayment_order_info')
        if self.repayment_order_info:
            for k in self.repayment_order_info:
                if k:
                    k.validate()
        self.validate_required(self.flow_id, 'flow_id')
        self.validate_required(self.user_tuid, 'user_tuid')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        result['repayment_order_info'] = []
        if self.repayment_order_info is not None:
            for k in self.repayment_order_info:
                result['repayment_order_info'].append(k.to_map() if k else None)
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.user_tuid is not None:
            result['user_tuid'] = self.user_tuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        self.repayment_order_info = []
        if m.get('repayment_order_info') is not None:
            for k in m.get('repayment_order_info'):
                temp_model = RepaymentOrderRequest()
                self.repayment_order_info.append(temp_model.from_map(k))
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('user_tuid') is not None:
            self.user_tuid = m.get('user_tuid')
        return self


class CreateContractCommontriggerResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        flow_id: str = None,
        platform_tuid: str = None,
        user_tuid: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 错误码
        self.code = code
        # 错误信息描述
        self.err_message = err_message
        # 合同id
        self.flow_id = flow_id
        # 商户在智能合同平台id
        self.platform_tuid = platform_tuid
        # 用户在智能合同平台的id
        self.user_tuid = user_tuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.platform_tuid is not None:
            result['platform_tuid'] = self.platform_tuid
        if self.user_tuid is not None:
            result['user_tuid'] = self.user_tuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('platform_tuid') is not None:
            self.platform_tuid = m.get('platform_tuid')
        if m.get('user_tuid') is not None:
            self.user_tuid = m.get('user_tuid')
        return self


class CreateContractMerchantindirectzftRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        biz_content: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 入驻材料
        self.biz_content = biz_content

    def validate(self):
        self.validate_required(self.biz_content, 'biz_content')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.biz_content is not None:
            result['biz_content'] = self.biz_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('biz_content') is not None:
            self.biz_content = m.get('biz_content')
        return self


class CreateContractMerchantindirectzftResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        body: str = None,
        code: int = None,
        message: str = None,
        order_id: str = None,
        sub_code: str = None,
        sub_msg: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 传入参数内容
        self.body = body
        # 错误码
        self.code = code
        # 错误信息描述
        self.message = message
        # 订单id
        self.order_id = order_id
        # 支付宝返回的二级错误信息
        self.sub_code = sub_code
        # 支付宝返回的二级错误信息描述
        self.sub_msg = sub_msg

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.body is not None:
            result['body'] = self.body
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.sub_code is not None:
            result['sub_code'] = self.sub_code
        if self.sub_msg is not None:
            result['sub_msg'] = self.sub_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('sub_code') is not None:
            self.sub_code = m.get('sub_code')
        if m.get('sub_msg') is not None:
            self.sub_msg = m.get('sub_msg')
        return self


class QueryContractMerchantindirectzftRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        order_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 商户入驻查询订单id
        self.order_id = order_id

    def validate(self):
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.order_id is not None:
            result['order_id'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        return self


class QueryContractMerchantindirectzftResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        ext_info: str = None,
        ip_role_id: List[str] = None,
        apply_id: str = None,
        merchant_name: str = None,
        status: str = None,
        sub_code: str = None,
        sub_msg: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 错误状态码，0表示成功
        self.code = code
        # 错误信息描述
        self.message = message
        # 额外信息，包含smid
        self.ext_info = ext_info
        # 支付宝的ipRoleId
        self.ip_role_id = ip_role_id
        # 申请时间
        self.apply_id = apply_id
        # 商户名称
        self.merchant_name = merchant_name
        # 直付通商户进件的状态
        self.status = status
        # 支付宝返回的错误状态码
        self.sub_code = sub_code
        # 支付宝返回的错误信息描述
        self.sub_msg = sub_msg

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.ext_info is not None:
            result['ext_info'] = self.ext_info
        if self.ip_role_id is not None:
            result['ip_role_id'] = self.ip_role_id
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.merchant_name is not None:
            result['merchant_name'] = self.merchant_name
        if self.status is not None:
            result['status'] = self.status
        if self.sub_code is not None:
            result['sub_code'] = self.sub_code
        if self.sub_msg is not None:
            result['sub_msg'] = self.sub_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('ext_info') is not None:
            self.ext_info = m.get('ext_info')
        if m.get('ip_role_id') is not None:
            self.ip_role_id = m.get('ip_role_id')
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('merchant_name') is not None:
            self.merchant_name = m.get('merchant_name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('sub_code') is not None:
            self.sub_code = m.get('sub_code')
        if m.get('sub_msg') is not None:
            self.sub_msg = m.get('sub_msg')
        return self


class QueryPayresultfileurlRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        bill_date: str = None,
        bill_type: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 对账日期
        self.bill_date = bill_date
        # 交易类型
        self.bill_type = bill_type

    def validate(self):
        self.validate_required(self.bill_date, 'bill_date')
        self.validate_required(self.bill_type, 'bill_type')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.bill_date is not None:
            result['bill_date'] = self.bill_date
        if self.bill_type is not None:
            result['bill_type'] = self.bill_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('bill_date') is not None:
            self.bill_date = m.get('bill_date')
        if m.get('bill_type') is not None:
            self.bill_type = m.get('bill_type')
        return self


class QueryPayresultfileurlResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        pay_url: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 对账文件的下载地址
        self.pay_url = pay_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.pay_url is not None:
            result['pay_url'] = self.pay_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('pay_url') is not None:
            self.pay_url = m.get('pay_url')
        return self


class CreateContractMerchantimageRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        content: str = None,
        file_name: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 图片内容，base64
        self.content = content
        # 图片名称
        self.file_name = file_name

    def validate(self):
        self.validate_required(self.content, 'content')
        self.validate_required(self.file_name, 'file_name')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.content is not None:
            result['content'] = self.content
        if self.file_name is not None:
            result['file_name'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        return self


class CreateContractMerchantimageResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        image_id: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 图片在oss上的id
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.image_id is not None:
            result['image_id'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')
        return self


class CancelContractPaytradeRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        flow_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 智能合同id
        self.flow_id = flow_id

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        return self


class CancelContractPaytradeResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        canceled_out_trade_no: List[str] = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 错误码
        self.code = code
        # 错误信息描述
        self.err_message = err_message
        # 取消的代扣条目
        self.canceled_out_trade_no = canceled_out_trade_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.canceled_out_trade_no is not None:
            result['canceled_out_trade_no'] = self.canceled_out_trade_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('canceled_out_trade_no') is not None:
            self.canceled_out_trade_no = m.get('canceled_out_trade_no')
        return self


class CreateContractHandsignflowRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        auto_archive: bool = None,
        business_scene: str = None,
        config_info: ContractSignFlowConfig = None,
        contract_remind: int = None,
        contract_validity: int = None,
        initiator_account_id: str = None,
        initiator_authorized_account_id: str = None,
        sign_validity: int = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 是否自动归档，默认false。如设置为true，当所有签署人签署完毕，系统自动将流程归档，状态变为“已完成”状态，在流程状态为“已完成”前，可随时添加签署人；如设置为false，则在调用签署流程开启后，需主动调用签署流程归档接口，将流程状态变更为“已完成”，归档前可随时添加签署人；已完成的流程才可下载签署后的文件。
        self.auto_archive = auto_archive
        # 文件主题
        self.business_scene = business_scene
        # 任务配置信息
        self.config_info = config_info
        # 文件到期前，提前多久回调提醒续签，单位为小时，时间区间：1小时——15天（360小时），默认不提醒
        self.contract_remind = contract_remind
        # 文件有效截止日期,毫秒，默认不失效
        self.contract_validity = contract_validity
        # 发起人账户id，即发起本次签署的操作人个人账号id；如不传，默认由对接平台发起
        self.initiator_account_id = initiator_account_id
        # 发起方主体id，如存在个人代机构发起签约，则需传入机构id；如不传，则默认是对接平台
        self.initiator_authorized_account_id = initiator_authorized_account_id
        # 签署有效截止日期,毫秒，默认不失效
        self.sign_validity = sign_validity

    def validate(self):
        self.validate_required(self.business_scene, 'business_scene')
        if self.config_info:
            self.config_info.validate()

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.auto_archive is not None:
            result['auto_archive'] = self.auto_archive
        if self.business_scene is not None:
            result['business_scene'] = self.business_scene
        if self.config_info is not None:
            result['config_info'] = self.config_info.to_map()
        if self.contract_remind is not None:
            result['contract_remind'] = self.contract_remind
        if self.contract_validity is not None:
            result['contract_validity'] = self.contract_validity
        if self.initiator_account_id is not None:
            result['initiator_account_id'] = self.initiator_account_id
        if self.initiator_authorized_account_id is not None:
            result['initiator_authorized_account_id'] = self.initiator_authorized_account_id
        if self.sign_validity is not None:
            result['sign_validity'] = self.sign_validity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('auto_archive') is not None:
            self.auto_archive = m.get('auto_archive')
        if m.get('business_scene') is not None:
            self.business_scene = m.get('business_scene')
        if m.get('config_info') is not None:
            temp_model = ContractSignFlowConfig()
            self.config_info = temp_model.from_map(m['config_info'])
        if m.get('contract_remind') is not None:
            self.contract_remind = m.get('contract_remind')
        if m.get('contract_validity') is not None:
            self.contract_validity = m.get('contract_validity')
        if m.get('initiator_account_id') is not None:
            self.initiator_account_id = m.get('initiator_account_id')
        if m.get('initiator_authorized_account_id') is not None:
            self.initiator_authorized_account_id = m.get('initiator_authorized_account_id')
        if m.get('sign_validity') is not None:
            self.sign_validity = m.get('sign_validity')
        return self


class CreateContractHandsignflowResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        flow_id: str = None,
        message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 流程ID
        self.flow_id = flow_id
        # 业务码信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateContractHandsignfieldRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        flow_id: str = None,
        sign_fields: List[ContractHandSignFieldApplication] = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 流程id
        self.flow_id = flow_id
        # 签署区列表数据
        self.sign_fields = sign_fields

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')
        self.validate_required(self.sign_fields, 'sign_fields')
        if self.sign_fields:
            for k in self.sign_fields:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        result['sign_fields'] = []
        if self.sign_fields is not None:
            for k in self.sign_fields:
                result['sign_fields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        self.sign_fields = []
        if m.get('sign_fields') is not None:
            for k in m.get('sign_fields'):
                temp_model = ContractHandSignFieldApplication()
                self.sign_fields.append(temp_model.from_map(k))
        return self


class CreateContractHandsignfieldResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        signfields: List[ContractSignField] = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message
        # 签署区列表数据
        self.signfields = signfields

    def validate(self):
        if self.signfields:
            for k in self.signfields:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        result['signfields'] = []
        if self.signfields is not None:
            for k in self.signfields:
                result['signfields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        self.signfields = []
        if m.get('signfields') is not None:
            for k in m.get('signfields'):
                temp_model = ContractSignField()
                self.signfields.append(temp_model.from_map(k))
        return self


class GetContractSignurlRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        account_id: str = None,
        flow_id: str = None,
        organize_id: str = None,
        short_url: bool = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 签署人账号id
        self.account_id = account_id
        # 流程id
        self.flow_id = flow_id
        # 默认为空，返回的任务链接仅包含签署人本人需要签署的任务； 传入0，则返回的任务链接包含签署人“本人+所有代签机构”的签署任务； 传入指定机构id，则返回的任务链接包含签署人“本人+指定代签机构”的签署任务
        self.organize_id = organize_id
        # 是否需要同时返回短链接，默认为false
        self.short_url = short_url

    def validate(self):
        self.validate_required(self.account_id, 'account_id')
        self.validate_required(self.flow_id, 'flow_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.account_id is not None:
            result['account_id'] = self.account_id
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.organize_id is not None:
            result['organize_id'] = self.organize_id
        if self.short_url is not None:
            result['short_url'] = self.short_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('account_id') is not None:
            self.account_id = m.get('account_id')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('organize_id') is not None:
            self.organize_id = m.get('organize_id')
        if m.get('short_url') is not None:
            self.short_url = m.get('short_url')
        return self


class GetContractSignurlResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        url: str = None,
        short_url: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message
        # 长链地址
        self.url = url
        # 短链地址
        self.short_url = short_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.url is not None:
            result['url'] = self.url
        if self.short_url is not None:
            result['short_url'] = self.short_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('short_url') is not None:
            self.short_url = m.get('short_url')
        return self


class CreateWithholdAgreementRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        credit_amount: str = None,
        external_agreement_no: str = None,
        merchant_id: str = None,
        merchant_name: str = None,
        merchant_service_description: str = None,
        merchant_service_name: str = None,
        name_cert_hash: str = None,
        repayment_url: str = None,
        return_url: str = None,
        third_party_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 授信总金额，单位元
        self.credit_amount = credit_amount
        # 商户签约号，代扣协议中标示用户的唯一签约号（确保在商户系统中唯一）
        self.external_agreement_no = external_agreement_no
        # 收款方账号类型，可取值：ALIPAY_USER_ID（支付宝uid);商户id，2088123412341234
        self.merchant_id = merchant_id
        # 商户名称
        self.merchant_name = merchant_name
        # 对服务产品的描述
        self.merchant_service_description = merchant_service_description
        # 商户的服务名称，滴滴出行免密支付
        self.merchant_service_name = merchant_service_name
        # 姓名和身份证号拼接sha256的hash
        self.name_cert_hash = name_cert_hash
        # 还款计划的链接
        self.repayment_url = repayment_url
        # 签约成功后回调的地址
        self.return_url = return_url
        # 第三方用户id
        self.third_party_id = third_party_id

    def validate(self):
        self.validate_required(self.credit_amount, 'credit_amount')
        self.validate_required(self.external_agreement_no, 'external_agreement_no')
        self.validate_required(self.merchant_id, 'merchant_id')
        self.validate_required(self.merchant_name, 'merchant_name')
        self.validate_required(self.merchant_service_name, 'merchant_service_name')
        self.validate_required(self.name_cert_hash, 'name_cert_hash')
        self.validate_required(self.repayment_url, 'repayment_url')
        self.validate_required(self.third_party_id, 'third_party_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.credit_amount is not None:
            result['credit_amount'] = self.credit_amount
        if self.external_agreement_no is not None:
            result['external_agreement_no'] = self.external_agreement_no
        if self.merchant_id is not None:
            result['merchant_id'] = self.merchant_id
        if self.merchant_name is not None:
            result['merchant_name'] = self.merchant_name
        if self.merchant_service_description is not None:
            result['merchant_service_description'] = self.merchant_service_description
        if self.merchant_service_name is not None:
            result['merchant_service_name'] = self.merchant_service_name
        if self.name_cert_hash is not None:
            result['name_cert_hash'] = self.name_cert_hash
        if self.repayment_url is not None:
            result['repayment_url'] = self.repayment_url
        if self.return_url is not None:
            result['return_url'] = self.return_url
        if self.third_party_id is not None:
            result['third_party_id'] = self.third_party_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('credit_amount') is not None:
            self.credit_amount = m.get('credit_amount')
        if m.get('external_agreement_no') is not None:
            self.external_agreement_no = m.get('external_agreement_no')
        if m.get('merchant_id') is not None:
            self.merchant_id = m.get('merchant_id')
        if m.get('merchant_name') is not None:
            self.merchant_name = m.get('merchant_name')
        if m.get('merchant_service_description') is not None:
            self.merchant_service_description = m.get('merchant_service_description')
        if m.get('merchant_service_name') is not None:
            self.merchant_service_name = m.get('merchant_service_name')
        if m.get('name_cert_hash') is not None:
            self.name_cert_hash = m.get('name_cert_hash')
        if m.get('repayment_url') is not None:
            self.repayment_url = m.get('repayment_url')
        if m.get('return_url') is not None:
            self.return_url = m.get('return_url')
        if m.get('third_party_id') is not None:
            self.third_party_id = m.get('third_party_id')
        return self


class CreateWithholdAgreementResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        return self


class QueryWithholdAgreementRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        external_agreement_no: str = None,
        third_party_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 商户签约号，代扣协议中标示用户的唯一签约号（确保在商户系统中唯一）
        self.external_agreement_no = external_agreement_no
        # 第三方用户id
        self.third_party_id = third_party_id

    def validate(self):
        self.validate_required(self.external_agreement_no, 'external_agreement_no')
        self.validate_required(self.third_party_id, 'third_party_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.external_agreement_no is not None:
            result['external_agreement_no'] = self.external_agreement_no
        if self.third_party_id is not None:
            result['third_party_id'] = self.third_party_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('external_agreement_no') is not None:
            self.external_agreement_no = m.get('external_agreement_no')
        if m.get('third_party_id') is not None:
            self.third_party_id = m.get('third_party_id')
        return self


class QueryWithholdAgreementResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        credit_amount: str = None,
        merchant_id: str = None,
        merchant_name: str = None,
        merchant_service_name: str = None,
        name_cert_hash: str = None,
        repayment_url: str = None,
        status: str = None,
        third_party_id: str = None,
        external_agreement_no: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 总授信金额
        self.credit_amount = credit_amount
        # 商家的支付宝uid
        self.merchant_id = merchant_id
        # 商户名称
        self.merchant_name = merchant_name
        # 商户的服务名称
        self.merchant_service_name = merchant_service_name
        # 姓名身份证号拼接后的hash
        self.name_cert_hash = name_cert_hash
        # 还款计划的超链接
        self.repayment_url = repayment_url
        # 协议的状态，如果签署成功返回success,未签是空
        self.status = status
        # 第三方的用户id
        self.third_party_id = third_party_id
        # 商家请求的协议号
        self.external_agreement_no = external_agreement_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.credit_amount is not None:
            result['credit_amount'] = self.credit_amount
        if self.merchant_id is not None:
            result['merchant_id'] = self.merchant_id
        if self.merchant_name is not None:
            result['merchant_name'] = self.merchant_name
        if self.merchant_service_name is not None:
            result['merchant_service_name'] = self.merchant_service_name
        if self.name_cert_hash is not None:
            result['name_cert_hash'] = self.name_cert_hash
        if self.repayment_url is not None:
            result['repayment_url'] = self.repayment_url
        if self.status is not None:
            result['status'] = self.status
        if self.third_party_id is not None:
            result['third_party_id'] = self.third_party_id
        if self.external_agreement_no is not None:
            result['external_agreement_no'] = self.external_agreement_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('credit_amount') is not None:
            self.credit_amount = m.get('credit_amount')
        if m.get('merchant_id') is not None:
            self.merchant_id = m.get('merchant_id')
        if m.get('merchant_name') is not None:
            self.merchant_name = m.get('merchant_name')
        if m.get('merchant_service_name') is not None:
            self.merchant_service_name = m.get('merchant_service_name')
        if m.get('name_cert_hash') is not None:
            self.name_cert_hash = m.get('name_cert_hash')
        if m.get('repayment_url') is not None:
            self.repayment_url = m.get('repayment_url')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('third_party_id') is not None:
            self.third_party_id = m.get('third_party_id')
        if m.get('external_agreement_no') is not None:
            self.external_agreement_no = m.get('external_agreement_no')
        return self


class QueryWithholdAgreementurlRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        external_agreement_no: str = None,
        third_party_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 商户签约号，代扣协议中标示用户的唯一签约号（确保在商户系统中唯一）
        self.external_agreement_no = external_agreement_no
        # 第三方用户id
        self.third_party_id = third_party_id

    def validate(self):
        self.validate_required(self.external_agreement_no, 'external_agreement_no')
        self.validate_required(self.third_party_id, 'third_party_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.external_agreement_no is not None:
            result['external_agreement_no'] = self.external_agreement_no
        if self.third_party_id is not None:
            result['third_party_id'] = self.third_party_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('external_agreement_no') is not None:
            self.external_agreement_no = m.get('external_agreement_no')
        if m.get('third_party_id') is not None:
            self.third_party_id = m.get('third_party_id')
        return self


class QueryWithholdAgreementurlResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        result_message: str = None,
        url: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 成功
        self.result_message = result_message
        # 代扣协议签署的入口
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.result_message is not None:
            result['result_message'] = self.result_message
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('result_message') is not None:
            self.result_message = m.get('result_message')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class CreateWithholdOverduetimeRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        merchant_id: str = None,
        merchant_name: str = None,
        merchant_service_name: str = None,
        tenant_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 首款方id
        self.merchant_id = merchant_id
        # 商家名称
        self.merchant_name = merchant_name
        # 商家提供的产品名称
        self.merchant_service_name = merchant_service_name
        # 租户id
        self.tenant_id = tenant_id

    def validate(self):
        self.validate_required(self.merchant_id, 'merchant_id')
        self.validate_required(self.merchant_name, 'merchant_name')
        self.validate_required(self.merchant_service_name, 'merchant_service_name')
        self.validate_required(self.tenant_id, 'tenant_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.merchant_id is not None:
            result['merchant_id'] = self.merchant_id
        if self.merchant_name is not None:
            result['merchant_name'] = self.merchant_name
        if self.merchant_service_name is not None:
            result['merchant_service_name'] = self.merchant_service_name
        if self.tenant_id is not None:
            result['tenant_id'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('merchant_id') is not None:
            self.merchant_id = m.get('merchant_id')
        if m.get('merchant_name') is not None:
            self.merchant_name = m.get('merchant_name')
        if m.get('merchant_service_name') is not None:
            self.merchant_service_name = m.get('merchant_service_name')
        if m.get('tenant_id') is not None:
            self.tenant_id = m.get('tenant_id')
        return self


class CreateWithholdOverduetimeResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        return self


class SendWithholdDeductRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        amount: str = None,
        business_params: str = None,
        external_agreement_no: str = None,
        order_title: str = None,
        out_biz_no: str = None,
        remark: str = None,
        third_party_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 委托支付订单总金额，单位为元，精确到小数点后两位
        self.amount = amount
        # JSON格式，传递业务扩展参数
        self.business_params = business_params
        # 商户签约号，代扣协议中标示用户的唯一签约号（确保在商户系统中唯一）
        self.external_agreement_no = external_agreement_no
        # 订单标题信息
        self.order_title = order_title
        # 外部订单号,请求方保证唯一性
        self.out_biz_no = out_biz_no
        # 备注
        self.remark = remark
        # 第三方的用户id
        self.third_party_id = third_party_id

    def validate(self):
        self.validate_required(self.amount, 'amount')
        self.validate_required(self.external_agreement_no, 'external_agreement_no')
        self.validate_required(self.out_biz_no, 'out_biz_no')
        self.validate_required(self.third_party_id, 'third_party_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.amount is not None:
            result['amount'] = self.amount
        if self.business_params is not None:
            result['business_params'] = self.business_params
        if self.external_agreement_no is not None:
            result['external_agreement_no'] = self.external_agreement_no
        if self.order_title is not None:
            result['order_title'] = self.order_title
        if self.out_biz_no is not None:
            result['out_biz_no'] = self.out_biz_no
        if self.remark is not None:
            result['remark'] = self.remark
        if self.third_party_id is not None:
            result['third_party_id'] = self.third_party_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('business_params') is not None:
            self.business_params = m.get('business_params')
        if m.get('external_agreement_no') is not None:
            self.external_agreement_no = m.get('external_agreement_no')
        if m.get('order_title') is not None:
            self.order_title = m.get('order_title')
        if m.get('out_biz_no') is not None:
            self.out_biz_no = m.get('out_biz_no')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('third_party_id') is not None:
            self.third_party_id = m.get('third_party_id')
        return self


class SendWithholdDeductResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        entrust_order_id: str = None,
        status: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 该笔转账在支付宝系统内部的单据ID
        self.entrust_order_id = entrust_order_id
        # INIT：受理成功，扣款中
        # FINISHED：扣款成功
        # CLOSED：商户已关单
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.entrust_order_id is not None:
            result['entrust_order_id'] = self.entrust_order_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('entrust_order_id') is not None:
            self.entrust_order_id = m.get('entrust_order_id')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class QueryWithholdPayresultRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        entrust_order_id: str = None,
        out_biz_no: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 请求扣款时，返回的委托单号,该笔转账在支付宝系统内部的单据ID
        self.entrust_order_id = entrust_order_id
        # 外部订单号,请求方保证唯一性
        self.out_biz_no = out_biz_no

    def validate(self):
        self.validate_required(self.entrust_order_id, 'entrust_order_id')
        self.validate_required(self.out_biz_no, 'out_biz_no')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.entrust_order_id is not None:
            result['entrust_order_id'] = self.entrust_order_id
        if self.out_biz_no is not None:
            result['out_biz_no'] = self.out_biz_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('entrust_order_id') is not None:
            self.entrust_order_id = m.get('entrust_order_id')
        if m.get('out_biz_no') is not None:
            self.out_biz_no = m.get('out_biz_no')
        return self


class QueryWithholdPayresultResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        pay_date: str = None,
        pay_order_id: str = None,
        status: str = None,
        trans_amount: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 支付完成日期
        self.pay_date = pay_date
        # 支付宝支付单据号
        self.pay_order_id = pay_order_id
        # INIT：受理成功，扣款中
        # FINISHED：扣款成功
        # CLOSED：商户已关单
        self.status = status
        # 扣款金额
        self.trans_amount = trans_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.pay_date is not None:
            result['pay_date'] = self.pay_date
        if self.pay_order_id is not None:
            result['pay_order_id'] = self.pay_order_id
        if self.status is not None:
            result['status'] = self.status
        if self.trans_amount is not None:
            result['trans_amount'] = self.trans_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('pay_date') is not None:
            self.pay_date = m.get('pay_date')
        if m.get('pay_order_id') is not None:
            self.pay_order_id = m.get('pay_order_id')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('trans_amount') is not None:
            self.trans_amount = m.get('trans_amount')
        return self


class SendWithholdRefundRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        order_id: str = None,
        out_request_no: str = None,
        refund_amount: str = None,
        remark: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 支付宝支付单据号
        self.order_id = order_id
        # 外部订单号,请求方保证唯一性
        self.out_request_no = out_request_no
        # 需要退款的金额，该金额不能大于订单金额,单位为元，支持两位小数
        self.refund_amount = refund_amount
        # 退款备注
        self.remark = remark

    def validate(self):
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.out_request_no, 'out_request_no')
        self.validate_required(self.refund_amount, 'refund_amount')
        self.validate_required(self.remark, 'remark')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.out_request_no is not None:
            result['out_request_no'] = self.out_request_no
        if self.refund_amount is not None:
            result['refund_amount'] = self.refund_amount
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('out_request_no') is not None:
            self.out_request_no = m.get('out_request_no')
        if m.get('refund_amount') is not None:
            self.refund_amount = m.get('refund_amount')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class SendWithholdRefundResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        refund_amount: str = None,
        refund_date: str = None,
        refund_order_id: str = None,
        status: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 需要退款的金额，该金额不能大于订单金额,单位为元，支持两位小数
        self.refund_amount = refund_amount
        # 退款成功的日期
        self.refund_date = refund_date
        # 退款的支付宝系统内部单据id
        self.refund_order_id = refund_order_id
        # FINISHED,退款成功的状态值
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.refund_amount is not None:
            result['refund_amount'] = self.refund_amount
        if self.refund_date is not None:
            result['refund_date'] = self.refund_date
        if self.refund_order_id is not None:
            result['refund_order_id'] = self.refund_order_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('refund_amount') is not None:
            self.refund_amount = m.get('refund_amount')
        if m.get('refund_date') is not None:
            self.refund_date = m.get('refund_date')
        if m.get('refund_order_id') is not None:
            self.refund_order_id = m.get('refund_order_id')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class SendContractInvitationRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        biz_process_id: str = None,
        callback_url: str = None,
        email: str = None,
        id_number: str = None,
        invitee_cert_type: str = None,
        invite_type: str = None,
        legal_cert_type: str = None,
        legal_name: str = None,
        legal_no: str = None,
        mobile: str = None,
        name: str = None,
        notify_type: str = None,
        organ_cert_no: str = None,
        organ_cert_type: str = None,
        organ_name: str = None,
        redirect_url: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 业务方id，重定向和回调时都回传这个id
        self.biz_process_id = biz_process_id
        # 回调接口地址，默认为空，不回调
        self.callback_url = callback_url
        # 被邀请人邮箱，若手机号和邮箱都传入，则仅手机号有效
        self.email = email
        # 被邀请人证件号
        self.id_number = id_number
        # 被邀请人证件类型，详见个人证件类型说明 ，默认CRED_PSN_CH_IDCARD
        self.invitee_cert_type = invitee_cert_type
        # 邀请个人实名为PERSON，邀请企业为ORGAN
        self.invite_type = invite_type
        # 企业法定代表人证件类型，详见个人证件类型说明 ，默认CRED_PSN_CH_IDCARD
        self.legal_cert_type = legal_cert_type
        # 企业法定代表人姓名
        self.legal_name = legal_name
        # 企业法定代表人证件号
        self.legal_no = legal_no
        # 被邀请人手机号
        self.mobile = mobile
        # 被邀请人姓名
        self.name = name
        # 默认为空，传入“sms”表示短信，“email”表示邮件，若两者都传入，则只发送短信
        self.notify_type = notify_type
        # 企业证件号
        self.organ_cert_no = organ_cert_no
        # 企业证件类型，详见机构证件类型说明 ，默认CRED_ORG_USCC
        self.organ_cert_type = organ_cert_type
        # 企业名称
        self.organ_name = organ_name
        # 结束后重定向地址（需加前缀https:// 或 http:// ），默认停留在当前页面
        self.redirect_url = redirect_url

    def validate(self):
        self.validate_required(self.invite_type, 'invite_type')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.biz_process_id is not None:
            result['biz_process_id'] = self.biz_process_id
        if self.callback_url is not None:
            result['callback_url'] = self.callback_url
        if self.email is not None:
            result['email'] = self.email
        if self.id_number is not None:
            result['id_number'] = self.id_number
        if self.invitee_cert_type is not None:
            result['invitee_cert_type'] = self.invitee_cert_type
        if self.invite_type is not None:
            result['invite_type'] = self.invite_type
        if self.legal_cert_type is not None:
            result['legal_cert_type'] = self.legal_cert_type
        if self.legal_name is not None:
            result['legal_name'] = self.legal_name
        if self.legal_no is not None:
            result['legal_no'] = self.legal_no
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.name is not None:
            result['name'] = self.name
        if self.notify_type is not None:
            result['notify_type'] = self.notify_type
        if self.organ_cert_no is not None:
            result['organ_cert_no'] = self.organ_cert_no
        if self.organ_cert_type is not None:
            result['organ_cert_type'] = self.organ_cert_type
        if self.organ_name is not None:
            result['organ_name'] = self.organ_name
        if self.redirect_url is not None:
            result['redirect_url'] = self.redirect_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('biz_process_id') is not None:
            self.biz_process_id = m.get('biz_process_id')
        if m.get('callback_url') is not None:
            self.callback_url = m.get('callback_url')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('id_number') is not None:
            self.id_number = m.get('id_number')
        if m.get('invitee_cert_type') is not None:
            self.invitee_cert_type = m.get('invitee_cert_type')
        if m.get('invite_type') is not None:
            self.invite_type = m.get('invite_type')
        if m.get('legal_cert_type') is not None:
            self.legal_cert_type = m.get('legal_cert_type')
        if m.get('legal_name') is not None:
            self.legal_name = m.get('legal_name')
        if m.get('legal_no') is not None:
            self.legal_no = m.get('legal_no')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('notify_type') is not None:
            self.notify_type = m.get('notify_type')
        if m.get('organ_cert_no') is not None:
            self.organ_cert_no = m.get('organ_cert_no')
        if m.get('organ_cert_type') is not None:
            self.organ_cert_type = m.get('organ_cert_type')
        if m.get('organ_name') is not None:
            self.organ_name = m.get('organ_name')
        if m.get('redirect_url') is not None:
            self.redirect_url = m.get('redirect_url')
        return self


class SendContractInvitationResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        invitation_id: str = None,
        invitation_url: str = None,
        message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 邀请任务id
        self.invitation_id = invitation_id
        # 邀请链接
        self.invitation_url = invitation_url
        # 业务码信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.invitation_id is not None:
            result['invitation_id'] = self.invitation_id
        if self.invitation_url is not None:
            result['invitation_url'] = self.invitation_url
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('invitation_id') is not None:
            self.invitation_id = m.get('invitation_id')
        if m.get('invitation_url') is not None:
            self.invitation_url = m.get('invitation_url')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListContractPayruleRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        flow_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # flowId
        self.flow_id = flow_id

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        return self


class ListContractPayruleResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 状态码，0表示成功
        self.code = code
        # ""
        self.err_message = err_message
        # 代扣规则描述json表示
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class CreateWithholdQrcodeRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        third_party_id: str = None,
        external_agreement_no: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 第三方的用户id
        self.third_party_id = third_party_id
        # 请求签约的协议号
        self.external_agreement_no = external_agreement_no

    def validate(self):
        self.validate_required(self.third_party_id, 'third_party_id')
        self.validate_required(self.external_agreement_no, 'external_agreement_no')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.third_party_id is not None:
            result['third_party_id'] = self.third_party_id
        if self.external_agreement_no is not None:
            result['external_agreement_no'] = self.external_agreement_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('third_party_id') is not None:
            self.third_party_id = m.get('third_party_id')
        if m.get('external_agreement_no') is not None:
            self.external_agreement_no = m.get('external_agreement_no')
        return self


class CreateWithholdQrcodeResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        qr_code_url: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 二维码图片链接地址
        self.qr_code_url = qr_code_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.qr_code_url is not None:
            result['qr_code_url'] = self.qr_code_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('qr_code_url') is not None:
            self.qr_code_url = m.get('qr_code_url')
        return self


class CancelContractPaysingletradeRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        flow_id: str = None,
        cancel_out_order_no: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 智能合同id
        self.flow_id = flow_id
        # 被取消的某一期的代扣id
        self.cancel_out_order_no = cancel_out_order_no

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')
        self.validate_required(self.cancel_out_order_no, 'cancel_out_order_no')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.cancel_out_order_no is not None:
            result['cancel_out_order_no'] = self.cancel_out_order_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('cancel_out_order_no') is not None:
            self.cancel_out_order_no = m.get('cancel_out_order_no')
        return self


class CancelContractPaysingletradeResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        canceled_out_trade_no: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 错误码，0表示成功
        self.code = code
        # 错误信息描述
        self.err_message = err_message
        # 被取消的某一期代扣订单id
        self.canceled_out_trade_no = canceled_out_trade_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.canceled_out_trade_no is not None:
            result['canceled_out_trade_no'] = self.canceled_out_trade_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('canceled_out_trade_no') is not None:
            self.canceled_out_trade_no = m.get('canceled_out_trade_no')
        return self


class ApplyContractCallbackkeyRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        return self


class ApplyContractCallbackkeyResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        key: str = None,
        code: int = None,
        message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 加签使用的key
        self.key = key
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.key is not None:
            result['key'] = self.key
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateContractOnestepflowRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        auto_archive: bool = None,
        auto_initiate: bool = None,
        business_scene: str = None,
        comment: str = None,
        contract_sign_flow_config: ContractSignFlowConfig = None,
        docs: List[ContractDoc] = None,
        initiator_account_id: str = None,
        initiator_authorized_account_id: str = None,
        sign_fields: List[OneStepSignField] = None,
        sign_platform: str = None,
        sign_validity: int = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 是否自动归档，默认false。
        self.auto_archive = auto_archive
        # 是否自动开启，默认false。
        self.auto_initiate = auto_initiate
        # 文件主题
        self.business_scene = business_scene
        # 流程备注
        self.comment = comment
        # 任务配置信息
        self.contract_sign_flow_config = contract_sign_flow_config
        # 待签文档信息
        self.docs = docs
        # 发起人账户id，即发起本次签署的操作人个人账号id；如不传，默认由对接平台发起
        self.initiator_account_id = initiator_account_id
        # 发起方主体id，如存在个人代机构发起签约，则需传入机构id；如不传，则默认是对接平台
        self.initiator_authorized_account_id = initiator_authorized_account_id
        # 流程中的签署区信息
        self.sign_fields = sign_fields
        # 签署平台，ALIPAY（支付宝小程序）或H5，默认H5
        self.sign_platform = sign_platform
        # 签署有效截止日期，毫秒，默认3天失效
        self.sign_validity = sign_validity

    def validate(self):
        self.validate_required(self.business_scene, 'business_scene')
        if self.contract_sign_flow_config:
            self.contract_sign_flow_config.validate()
        if self.docs:
            for k in self.docs:
                if k:
                    k.validate()
        if self.sign_fields:
            for k in self.sign_fields:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.auto_archive is not None:
            result['auto_archive'] = self.auto_archive
        if self.auto_initiate is not None:
            result['auto_initiate'] = self.auto_initiate
        if self.business_scene is not None:
            result['business_scene'] = self.business_scene
        if self.comment is not None:
            result['comment'] = self.comment
        if self.contract_sign_flow_config is not None:
            result['contract_sign_flow_config'] = self.contract_sign_flow_config.to_map()
        result['docs'] = []
        if self.docs is not None:
            for k in self.docs:
                result['docs'].append(k.to_map() if k else None)
        if self.initiator_account_id is not None:
            result['initiator_account_id'] = self.initiator_account_id
        if self.initiator_authorized_account_id is not None:
            result['initiator_authorized_account_id'] = self.initiator_authorized_account_id
        result['sign_fields'] = []
        if self.sign_fields is not None:
            for k in self.sign_fields:
                result['sign_fields'].append(k.to_map() if k else None)
        if self.sign_platform is not None:
            result['sign_platform'] = self.sign_platform
        if self.sign_validity is not None:
            result['sign_validity'] = self.sign_validity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('auto_archive') is not None:
            self.auto_archive = m.get('auto_archive')
        if m.get('auto_initiate') is not None:
            self.auto_initiate = m.get('auto_initiate')
        if m.get('business_scene') is not None:
            self.business_scene = m.get('business_scene')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('contract_sign_flow_config') is not None:
            temp_model = ContractSignFlowConfig()
            self.contract_sign_flow_config = temp_model.from_map(m['contract_sign_flow_config'])
        self.docs = []
        if m.get('docs') is not None:
            for k in m.get('docs'):
                temp_model = ContractDoc()
                self.docs.append(temp_model.from_map(k))
        if m.get('initiator_account_id') is not None:
            self.initiator_account_id = m.get('initiator_account_id')
        if m.get('initiator_authorized_account_id') is not None:
            self.initiator_authorized_account_id = m.get('initiator_authorized_account_id')
        self.sign_fields = []
        if m.get('sign_fields') is not None:
            for k in m.get('sign_fields'):
                temp_model = OneStepSignField()
                self.sign_fields.append(temp_model.from_map(k))
        if m.get('sign_platform') is not None:
            self.sign_platform = m.get('sign_platform')
        if m.get('sign_validity') is not None:
            self.sign_validity = m.get('sign_validity')
        return self


class CreateContractOnestepflowResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        flow_id: str = None,
        message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 流程ID
        self.flow_id = flow_id
        # 业务码信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class QueryContractNotaryRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        flow_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 签署流程ID
        self.flow_id = flow_id

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        return self


class QueryContractNotaryResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        notaries: List[ContractNotaryInfo] = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message
        # 存证信息列表
        self.notaries = notaries

    def validate(self):
        if self.notaries:
            for k in self.notaries:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        result['notaries'] = []
        if self.notaries is not None:
            for k in self.notaries:
                result['notaries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        self.notaries = []
        if m.get('notaries') is not None:
            for k in m.get('notaries'):
                temp_model = ContractNotaryInfo()
                self.notaries.append(temp_model.from_map(k))
        return self


class CreateEcocontractTransRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        customer: Identity = None,
        properties: str = None,
        sub_biz_id: str = None,
        tsr: bool = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 存证关联实体（个人/企业）的身份识别信息
        self.customer = customer
        # 扩展属性
        self.properties = properties
        # 业务子类型标识
        self.sub_biz_id = sub_biz_id
        # 是否使用可信时间戳，默认为false
        self.tsr = tsr

    def validate(self):
        self.validate_required(self.customer, 'customer')
        if self.customer:
            self.customer.validate()

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.customer is not None:
            result['customer'] = self.customer.to_map()
        if self.properties is not None:
            result['properties'] = self.properties
        if self.sub_biz_id is not None:
            result['sub_biz_id'] = self.sub_biz_id
        if self.tsr is not None:
            result['tsr'] = self.tsr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('customer') is not None:
            temp_model = Identity()
            self.customer = temp_model.from_map(m['customer'])
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('sub_biz_id') is not None:
            self.sub_biz_id = m.get('sub_biz_id')
        if m.get('tsr') is not None:
            self.tsr = m.get('tsr')
        return self


class CreateEcocontractTransResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        transaction_id: str = None,
        tsr: TsrResponse = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 返回事务ID，全局唯一
        self.transaction_id = transaction_id
        # 可信时间信息
        self.tsr = tsr

    def validate(self):
        if self.tsr:
            self.tsr.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.tsr is not None:
            result['tsr'] = self.tsr.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('tsr') is not None:
            temp_model = TsrResponse()
            self.tsr = temp_model.from_map(m['tsr'])
        return self


class CreateEcocontractTextRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        finish_info: ContractNotaryFinishInfo = None,
        flow_id: str = None,
        init_info: ContractNotaryInitInfo = None,
        phase: str = None,
        sign_info: ContractNotarySignInfo = None,
        transaction_id: str = None,
        document_info: ContractNotaryDocumentInfo = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 签署结束信息，phase为FINISH时必选
        self.finish_info = finish_info
        # 签署流程ID
        self.flow_id = flow_id
        # 签署发起信息，phase为INIT时必选
        self.init_info = init_info
        # 存证阶段，分为INIT(发起)，SIGN(签署)，FINISH(结束)
        self.phase = phase
        # 签署过程信息，phase为SIGN时必选
        self.sign_info = sign_info
        # 存证事务ID
        self.transaction_id = transaction_id
        # 签署文件存档阶段存证核验信息
        self.document_info = document_info

    def validate(self):
        if self.finish_info:
            self.finish_info.validate()
        self.validate_required(self.flow_id, 'flow_id')
        if self.init_info:
            self.init_info.validate()
        self.validate_required(self.phase, 'phase')
        if self.sign_info:
            self.sign_info.validate()
        self.validate_required(self.transaction_id, 'transaction_id')
        if self.document_info:
            self.document_info.validate()

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.finish_info is not None:
            result['finish_info'] = self.finish_info.to_map()
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.init_info is not None:
            result['init_info'] = self.init_info.to_map()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.sign_info is not None:
            result['sign_info'] = self.sign_info.to_map()
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.document_info is not None:
            result['document_info'] = self.document_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('finish_info') is not None:
            temp_model = ContractNotaryFinishInfo()
            self.finish_info = temp_model.from_map(m['finish_info'])
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('init_info') is not None:
            temp_model = ContractNotaryInitInfo()
            self.init_info = temp_model.from_map(m['init_info'])
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('sign_info') is not None:
            temp_model = ContractNotarySignInfo()
            self.sign_info = temp_model.from_map(m['sign_info'])
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('document_info') is not None:
            temp_model = ContractNotaryDocumentInfo()
            self.document_info = temp_model.from_map(m['document_info'])
        return self


class CreateEcocontractTextResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        tx_hash: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 存证凭据,
        self.tx_hash = tx_hash

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class QueryContractWordspositionRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        file_id: str = None,
        keywords: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 文档id
        self.file_id = file_id
        # 关键字列表，逗号分割；注意要英文的逗号，不能中文逗号；关键字建议不要设置特殊字符，因Adobe无法识别部分符号，某些特殊字符会因解析失败从而导致搜索不到
        self.keywords = keywords

    def validate(self):
        self.validate_required(self.file_id, 'file_id')
        self.validate_required(self.keywords, 'keywords')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.keywords is not None:
            result['keywords'] = self.keywords
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('keywords') is not None:
            self.keywords = m.get('keywords')
        return self


class QueryContractWordspositionResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        file_id: str = None,
        data: List[KeywordsPosition] = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message
        # 文档id
        self.file_id = file_id
        # 关键字位置列表
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.file_id is not None:
            result['file_id'] = self.file_id
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = KeywordsPosition()
                self.data.append(temp_model.from_map(k))
        return self


class DeleteContractSignerRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        flow_id: str = None,
        account_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 签署流程ID
        self.flow_id = flow_id
        # 签署人ID
        self.account_id = account_id

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')
        self.validate_required(self.account_id, 'account_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.account_id is not None:
            result['account_id'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('account_id') is not None:
            self.account_id = m.get('account_id')
        return self


class DeleteContractSignerResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CheckEpidentityTwometaRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        ep_cert_name: str = None,
        ep_cert_no: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 认证企业名称。
        self.ep_cert_name = ep_cert_name
        # 企业证件号码。
        self.ep_cert_no = ep_cert_no

    def validate(self):
        self.validate_required(self.ep_cert_name, 'ep_cert_name')
        self.validate_required(self.ep_cert_no, 'ep_cert_no')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.ep_cert_name is not None:
            result['ep_cert_name'] = self.ep_cert_name
        if self.ep_cert_no is not None:
            result['ep_cert_no'] = self.ep_cert_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('ep_cert_name') is not None:
            self.ep_cert_name = m.get('ep_cert_name')
        if m.get('ep_cert_no') is not None:
            self.ep_cert_no = m.get('ep_cert_no')
        return self


class CheckEpidentityTwometaResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        enterprise_status: str = None,
        open_time: str = None,
        passed: bool = None,
        code: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 企业状态。
        self.enterprise_status = enterprise_status
        # 营业期限。
        self.open_time = open_time
        # 核验是否通过。
        self.passed = passed
        # 0:核验成功 1:企业信息有误 2:企业非正常营业
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.enterprise_status is not None:
            result['enterprise_status'] = self.enterprise_status
        if self.open_time is not None:
            result['open_time'] = self.open_time
        if self.passed is not None:
            result['passed'] = self.passed
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('enterprise_status') is not None:
            self.enterprise_status = m.get('enterprise_status')
        if m.get('open_time') is not None:
            self.open_time = m.get('open_time')
        if m.get('passed') is not None:
            self.passed = m.get('passed')
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class CheckEpidentityThreemetaRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        ep_cert_name: str = None,
        ep_cert_no: str = None,
        legal_person_cert_name: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 认证企业名称。
        self.ep_cert_name = ep_cert_name
        # 企业证件号码。
        self.ep_cert_no = ep_cert_no
        # 企业法人姓名。
        self.legal_person_cert_name = legal_person_cert_name

    def validate(self):
        self.validate_required(self.ep_cert_name, 'ep_cert_name')
        self.validate_required(self.ep_cert_no, 'ep_cert_no')
        self.validate_required(self.legal_person_cert_name, 'legal_person_cert_name')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.ep_cert_name is not None:
            result['ep_cert_name'] = self.ep_cert_name
        if self.ep_cert_no is not None:
            result['ep_cert_no'] = self.ep_cert_no
        if self.legal_person_cert_name is not None:
            result['legal_person_cert_name'] = self.legal_person_cert_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('ep_cert_name') is not None:
            self.ep_cert_name = m.get('ep_cert_name')
        if m.get('ep_cert_no') is not None:
            self.ep_cert_no = m.get('ep_cert_no')
        if m.get('legal_person_cert_name') is not None:
            self.legal_person_cert_name = m.get('legal_person_cert_name')
        return self


class CheckEpidentityThreemetaResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        enterprise_status: str = None,
        open_time: str = None,
        passed: bool = None,
        code: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 企业状态。
        self.enterprise_status = enterprise_status
        # 营业期限。
        self.open_time = open_time
        # 核验是否通过。
        self.passed = passed
        # 0:核验成功 1:企业信息有误 2:企业非正常营业
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.enterprise_status is not None:
            result['enterprise_status'] = self.enterprise_status
        if self.open_time is not None:
            result['open_time'] = self.open_time
        if self.passed is not None:
            result['passed'] = self.passed
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('enterprise_status') is not None:
            self.enterprise_status = m.get('enterprise_status')
        if m.get('open_time') is not None:
            self.open_time = m.get('open_time')
        if m.get('passed') is not None:
            self.passed = m.get('passed')
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class CheckEpidentityFourmetaRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        ep_cert_name: str = None,
        ep_cert_no: str = None,
        legal_person_cert_name: str = None,
        legal_person_cert_no: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 认证企业名称。
        self.ep_cert_name = ep_cert_name
        # 企业证件号码。
        self.ep_cert_no = ep_cert_no
        # 企业法人姓名。
        self.legal_person_cert_name = legal_person_cert_name
        # 企业法人身份证号码。
        self.legal_person_cert_no = legal_person_cert_no

    def validate(self):
        self.validate_required(self.ep_cert_name, 'ep_cert_name')
        self.validate_required(self.ep_cert_no, 'ep_cert_no')
        self.validate_required(self.legal_person_cert_name, 'legal_person_cert_name')
        self.validate_required(self.legal_person_cert_no, 'legal_person_cert_no')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.ep_cert_name is not None:
            result['ep_cert_name'] = self.ep_cert_name
        if self.ep_cert_no is not None:
            result['ep_cert_no'] = self.ep_cert_no
        if self.legal_person_cert_name is not None:
            result['legal_person_cert_name'] = self.legal_person_cert_name
        if self.legal_person_cert_no is not None:
            result['legal_person_cert_no'] = self.legal_person_cert_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('ep_cert_name') is not None:
            self.ep_cert_name = m.get('ep_cert_name')
        if m.get('ep_cert_no') is not None:
            self.ep_cert_no = m.get('ep_cert_no')
        if m.get('legal_person_cert_name') is not None:
            self.legal_person_cert_name = m.get('legal_person_cert_name')
        if m.get('legal_person_cert_no') is not None:
            self.legal_person_cert_no = m.get('legal_person_cert_no')
        return self


class CheckEpidentityFourmetaResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        enterprise_status: str = None,
        open_time: str = None,
        passed: bool = None,
        code: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 企业状态。
        self.enterprise_status = enterprise_status
        # 营业期限。
        self.open_time = open_time
        # 核验是否通过。
        self.passed = passed
        # 0:核验成功 1:企业信息有误 2:企业非正常营业
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.enterprise_status is not None:
            result['enterprise_status'] = self.enterprise_status
        if self.open_time is not None:
            result['open_time'] = self.open_time
        if self.passed is not None:
            result['passed'] = self.passed
        if self.code is not None:
            result['code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('enterprise_status') is not None:
            self.enterprise_status = m.get('enterprise_status')
        if m.get('open_time') is not None:
            self.open_time = m.get('open_time')
        if m.get('passed') is not None:
            self.passed = m.get('passed')
        if m.get('code') is not None:
            self.code = m.get('code')
        return self


class CheckNotarizationOrderRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        order_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 公证订单ID号
        self.order_id = order_id

    def validate(self):
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.order_id is not None:
            result['order_id'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        return self


class CheckNotarizationOrderResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        biz_id: List[str] = None,
        face_auth_code: str = None,
        user_id: str = None,
        valid: bool = None,
        org_id: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 下单的业务类型ID列表
        self.biz_id = biz_id
        # 实人认证接口调用授权码，与公证订单一一对应，有效次数默认为3次，超过调用次数则失效
        self.face_auth_code = face_auth_code
        # 下单客户的账号ID
        self.user_id = user_id
        # 是否为合法订单
        self.valid = valid
        # 平台公证机构ID
        self.org_id = org_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.biz_id is not None:
            result['biz_id'] = self.biz_id
        if self.face_auth_code is not None:
            result['face_auth_code'] = self.face_auth_code
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.valid is not None:
            result['valid'] = self.valid
        if self.org_id is not None:
            result['org_id'] = self.org_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('biz_id') is not None:
            self.biz_id = m.get('biz_id')
        if m.get('face_auth_code') is not None:
            self.face_auth_code = m.get('face_auth_code')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('valid') is not None:
            self.valid = m.get('valid')
        if m.get('org_id') is not None:
            self.org_id = m.get('org_id')
        return self


class UpdateNotarizationOrderRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        order_id: str = None,
        reason: str = None,
        status: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 公证订单ID
        self.order_id = order_id
        # 如果出证失败，需要给出失败原因
        self.reason = reason
        # 出证状态的枚举值
        self.status = status

    def validate(self):
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.reason is not None:
            result['reason'] = self.reason
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class UpdateNotarizationOrderResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        accepted: bool = None,
        reason: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 状态是否更新成功
        self.accepted = accepted
        # 如更新失败，返回失败原因
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.accepted is not None:
            result['accepted'] = self.accepted
        if self.reason is not None:
            result['reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('accepted') is not None:
            self.accepted = m.get('accepted')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        return self


class SetNotarizationOrderRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        biz_code: str = None,
        key: str = None,
        order_id: str = None,
        value: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 公证事项ID
        self.biz_code = biz_code
        # 需设置的属性名称
        self.key = key
        # 公证订单ID
        self.order_id = order_id
        # 被设置字段的值
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.biz_code is not None:
            result['biz_code'] = self.biz_code
        if self.key is not None:
            result['key'] = self.key
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('biz_code') is not None:
            self.biz_code = m.get('biz_code')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class SetNotarizationOrderResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        accepted: bool = None,
        reason: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 是否设置成功
        self.accepted = accepted
        # 如设置失败，返回失败原因
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.accepted is not None:
            result['accepted'] = self.accepted
        if self.reason is not None:
            result['reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('accepted') is not None:
            self.accepted = m.get('accepted')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        return self


class InitIdentificationFaceauthRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        cert_name: str = None,
        cert_no: str = None,
        auth_code: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 认证人的姓名
        self.cert_name = cert_name
        # 被验证者的身份证号码
        self.cert_no = cert_no
        # 授权码，针对某些特定场景使用，非必填
        self.auth_code = auth_code

    def validate(self):
        self.validate_required(self.cert_name, 'cert_name')
        self.validate_required(self.cert_no, 'cert_no')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.cert_name is not None:
            result['cert_name'] = self.cert_name
        if self.cert_no is not None:
            result['cert_no'] = self.cert_no
        if self.auth_code is not None:
            result['auth_code'] = self.auth_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('cert_name') is not None:
            self.cert_name = m.get('cert_name')
        if m.get('cert_no') is not None:
            self.cert_no = m.get('cert_no')
        if m.get('auth_code') is not None:
            self.auth_code = m.get('auth_code')
        return self


class InitIdentificationFaceauthResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        certify_id: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 发起一个实人认证流程，获取到流程ID
        self.certify_id = certify_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.certify_id is not None:
            result['certify_id'] = self.certify_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('certify_id') is not None:
            self.certify_id = m.get('certify_id')
        return self


class CertifyIdentificationFaceauthRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        certify_id: str = None,
        callback_url: str = None,
        redirect_url: str = None,
        auth_code: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 实人认证流程ID
        self.certify_id = certify_id
        # 认证流程结束回调通知地址，非必传
        self.callback_url = callback_url
        # 认证结束后跳转地址，非必填
        self.redirect_url = redirect_url
        # 授权码，针对某些特定场景使用，非必填
        self.auth_code = auth_code

    def validate(self):
        self.validate_required(self.certify_id, 'certify_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.certify_id is not None:
            result['certify_id'] = self.certify_id
        if self.callback_url is not None:
            result['callback_url'] = self.callback_url
        if self.redirect_url is not None:
            result['redirect_url'] = self.redirect_url
        if self.auth_code is not None:
            result['auth_code'] = self.auth_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('certify_id') is not None:
            self.certify_id = m.get('certify_id')
        if m.get('callback_url') is not None:
            self.callback_url = m.get('callback_url')
        if m.get('redirect_url') is not None:
            self.redirect_url = m.get('redirect_url')
        if m.get('auth_code') is not None:
            self.auth_code = m.get('auth_code')
        return self


class CertifyIdentificationFaceauthResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        certify_id: str = None,
        verify_url: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 实人认证流程ID
        self.certify_id = certify_id
        # 发起实人认证的地址
        self.verify_url = verify_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.certify_id is not None:
            result['certify_id'] = self.certify_id
        if self.verify_url is not None:
            result['verify_url'] = self.verify_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('certify_id') is not None:
            self.certify_id = m.get('certify_id')
        if m.get('verify_url') is not None:
            self.verify_url = m.get('verify_url')
        return self


class QueryIdentificationFaceauthRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        certify_id: str = None,
        auth_code: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 实人认证流程ID
        self.certify_id = certify_id
        # 授权码，针对某些特定场景使用，非必填
        self.auth_code = auth_code

    def validate(self):
        self.validate_required(self.certify_id, 'certify_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.certify_id is not None:
            result['certify_id'] = self.certify_id
        if self.auth_code is not None:
            result['auth_code'] = self.auth_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('certify_id') is not None:
            self.certify_id = m.get('certify_id')
        if m.get('auth_code') is not None:
            self.auth_code = m.get('auth_code')
        return self


class QueryIdentificationFaceauthResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        certify_id: str = None,
        passed: bool = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 实人认证流程ID
        self.certify_id = certify_id
        # 是否通过实人认证
        self.passed = passed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.certify_id is not None:
            result['certify_id'] = self.certify_id
        if self.passed is not None:
            result['passed'] = self.passed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('certify_id') is not None:
            self.certify_id = m.get('certify_id')
        if m.get('passed') is not None:
            self.passed = m.get('passed')
        return self


class QueryEnterpriseFaceauthRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        biz_no: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 企业法人认证查询
        self.biz_no = biz_no

    def validate(self):
        self.validate_required(self.biz_no, 'biz_no')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.biz_no is not None:
            result['biz_no'] = self.biz_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('biz_no') is not None:
            self.biz_no = m.get('biz_no')
        return self


class QueryEnterpriseFaceauthResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        biz_no: str = None,
        failed_code: str = None,
        passed: bool = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 认证唯一性标识
        self.biz_no = biz_no
        # 认证失败错误码
        self.failed_code = failed_code
        # 认证是否通过
        self.passed = passed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.biz_no is not None:
            result['biz_no'] = self.biz_no
        if self.failed_code is not None:
            result['failed_code'] = self.failed_code
        if self.passed is not None:
            result['passed'] = self.passed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('biz_no') is not None:
            self.biz_no = m.get('biz_no')
        if m.get('failed_code') is not None:
            self.failed_code = m.get('failed_code')
        if m.get('passed') is not None:
            self.passed = m.get('passed')
        return self


class InitEnterpriseFaceauthRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        ep_cert_name: str = None,
        ep_cert_no: str = None,
        ep_cert_type: str = None,
        legal_person_cert_name: str = None,
        legal_person_cert_no: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 企业名称
        self.ep_cert_name = ep_cert_name
        # 企业证件号
        self.ep_cert_no = ep_cert_no
        # 企业证件类型（NATIONAL_LEGAL（工商注册号）或 NATIONAL_LEGAL_MERGE （ 社会统一信用代码））
        self.ep_cert_type = ep_cert_type
        # 企业法人姓名
        self.legal_person_cert_name = legal_person_cert_name
        # 企业法人身份证号（目前仅支持身份证号）
        self.legal_person_cert_no = legal_person_cert_no

    def validate(self):
        self.validate_required(self.ep_cert_name, 'ep_cert_name')
        self.validate_required(self.ep_cert_no, 'ep_cert_no')
        self.validate_required(self.ep_cert_type, 'ep_cert_type')
        self.validate_required(self.legal_person_cert_name, 'legal_person_cert_name')
        self.validate_required(self.legal_person_cert_no, 'legal_person_cert_no')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.ep_cert_name is not None:
            result['ep_cert_name'] = self.ep_cert_name
        if self.ep_cert_no is not None:
            result['ep_cert_no'] = self.ep_cert_no
        if self.ep_cert_type is not None:
            result['ep_cert_type'] = self.ep_cert_type
        if self.legal_person_cert_name is not None:
            result['legal_person_cert_name'] = self.legal_person_cert_name
        if self.legal_person_cert_no is not None:
            result['legal_person_cert_no'] = self.legal_person_cert_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('ep_cert_name') is not None:
            self.ep_cert_name = m.get('ep_cert_name')
        if m.get('ep_cert_no') is not None:
            self.ep_cert_no = m.get('ep_cert_no')
        if m.get('ep_cert_type') is not None:
            self.ep_cert_type = m.get('ep_cert_type')
        if m.get('legal_person_cert_name') is not None:
            self.legal_person_cert_name = m.get('legal_person_cert_name')
        if m.get('legal_person_cert_no') is not None:
            self.legal_person_cert_no = m.get('legal_person_cert_no')
        return self


class InitEnterpriseFaceauthResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        biz_no: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 本次认证的业务唯一性标示
        self.biz_no = biz_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.biz_no is not None:
            result['biz_no'] = self.biz_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('biz_no') is not None:
            self.biz_no = m.get('biz_no')
        return self


class CertifyEnterpriseFaceauthRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        biz_no: str = None,
        callback_url: str = None,
        redirect_url: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 业务唯一性标识
        self.biz_no = biz_no
        # 回调通知地址
        self.callback_url = callback_url
        # 认证完成后回跳地址
        self.redirect_url = redirect_url

    def validate(self):
        self.validate_required(self.biz_no, 'biz_no')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.biz_no is not None:
            result['biz_no'] = self.biz_no
        if self.callback_url is not None:
            result['callback_url'] = self.callback_url
        if self.redirect_url is not None:
            result['redirect_url'] = self.redirect_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('biz_no') is not None:
            self.biz_no = m.get('biz_no')
        if m.get('callback_url') is not None:
            self.callback_url = m.get('callback_url')
        if m.get('redirect_url') is not None:
            self.redirect_url = m.get('redirect_url')
        return self


class CertifyEnterpriseFaceauthResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        biz_no: str = None,
        verify_url: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务唯一性标识
        self.biz_no = biz_no
        # 认证 url
        self.verify_url = verify_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.biz_no is not None:
            result['biz_no'] = self.biz_no
        if self.verify_url is not None:
            result['verify_url'] = self.verify_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('biz_no') is not None:
            self.biz_no = m.get('biz_no')
        if m.get('verify_url') is not None:
            self.verify_url = m.get('verify_url')
        return self


class CreateLeaseOrderRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        account_id: str = None,
        alipay_order_amount: int = None,
        alipay_order_no: str = None,
        alipay_order_total_amount: int = None,
        deposit_waive_amount: int = None,
        insurance_coverage: int = None,
        insurance_order_no: str = None,
        item_name: str = None,
        item_price: int = None,
        item_type: str = None,
        merchant_alipay_account: str = None,
        merchant_alipay_id: str = None,
        merchant_name: str = None,
        merchant_order_no: str = None,
        payment_channel: str = None,
        tenancy_term_end: int = None,
        tenancy_term_start: int = None,
        insured: bool = None,
        insurance_order_url: str = None,
        insurance_bill_no: str = None,
        insurance_bill_time: str = None,
        insurance_bill_amount: int = None,
        insurance_product_coverage: int = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 账号标识，可弃用
        self.account_id = account_id
        # 支付宝交易金额
        self.alipay_order_amount = alipay_order_amount
        # 支付宝订单号
        self.alipay_order_no = alipay_order_no
        # 支付宝交易总金额
        self.alipay_order_total_amount = alipay_order_total_amount
        # 免押金额
        self.deposit_waive_amount = deposit_waive_amount
        # 订单总保额，单位分，insured为True时必填
        self.insurance_coverage = insurance_coverage
        # 保单号，insured为True时必填，仅支持数字和字母
        self.insurance_order_no = insurance_order_no
        # 商品名称
        self.item_name = item_name
        # 商品市场价格
        self.item_price = item_price
        # 商品类目
        self.item_type = item_type
        # 商户支付宝账号
        self.merchant_alipay_account = merchant_alipay_account
        # 商户支付宝ID
        self.merchant_alipay_id = merchant_alipay_id
        # 商户名称
        self.merchant_name = merchant_name
        # 商户单号
        self.merchant_order_no = merchant_order_no
        # 支付渠道，包括支付宝（Alipay）、第三方收单机构（ThirdParty）、信用卡（CreditCard）、银行转账（BankTransfer）、微信（WeChatPay）、其他（Other）
        self.payment_channel = payment_channel
        # 租约结束日期
        self.tenancy_term_end = tenancy_term_end
        # 租约起始日期
        self.tenancy_term_start = tenancy_term_start
        # 是否投保，默认为True
        self.insured = insured
        # 保单查询地址，insured为True时必填
        self.insurance_order_url = insurance_order_url
        # 保险缴费单号，insured为True时必填，仅支持数字和字母，长度20
        self.insurance_bill_no = insurance_bill_no
        # 保险缴费北京时间，格式为"YYYYMMDDHHMISS"，时区为UTC+8
        self.insurance_bill_time = insurance_bill_time
        # 保险缴费金额，单位分
        self.insurance_bill_amount = insurance_bill_amount
        # 订单产品保额，单位分，insured为True时必填
        self.insurance_product_coverage = insurance_product_coverage

    def validate(self):
        self.validate_required(self.alipay_order_amount, 'alipay_order_amount')
        if self.alipay_order_amount is not None:
            self.validate_minimum(self.alipay_order_amount, 'alipay_order_amount', 0)
        self.validate_required(self.alipay_order_no, 'alipay_order_no')
        self.validate_required(self.alipay_order_total_amount, 'alipay_order_total_amount')
        if self.alipay_order_total_amount is not None:
            self.validate_minimum(self.alipay_order_total_amount, 'alipay_order_total_amount', 0)
        self.validate_required(self.deposit_waive_amount, 'deposit_waive_amount')
        if self.deposit_waive_amount is not None:
            self.validate_minimum(self.deposit_waive_amount, 'deposit_waive_amount', 0)
        if self.insurance_coverage is not None:
            self.validate_minimum(self.insurance_coverage, 'insurance_coverage', 0)
        self.validate_required(self.item_name, 'item_name')
        self.validate_required(self.item_price, 'item_price')
        if self.item_price is not None:
            self.validate_minimum(self.item_price, 'item_price', 0)
        self.validate_required(self.item_type, 'item_type')
        self.validate_required(self.merchant_alipay_account, 'merchant_alipay_account')
        self.validate_required(self.merchant_alipay_id, 'merchant_alipay_id')
        self.validate_required(self.merchant_name, 'merchant_name')
        self.validate_required(self.tenancy_term_end, 'tenancy_term_end')
        if self.tenancy_term_end is not None:
            self.validate_minimum(self.tenancy_term_end, 'tenancy_term_end', 0)
        self.validate_required(self.tenancy_term_start, 'tenancy_term_start')
        if self.tenancy_term_start is not None:
            self.validate_minimum(self.tenancy_term_start, 'tenancy_term_start', 0)

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.account_id is not None:
            result['account_id'] = self.account_id
        if self.alipay_order_amount is not None:
            result['alipay_order_amount'] = self.alipay_order_amount
        if self.alipay_order_no is not None:
            result['alipay_order_no'] = self.alipay_order_no
        if self.alipay_order_total_amount is not None:
            result['alipay_order_total_amount'] = self.alipay_order_total_amount
        if self.deposit_waive_amount is not None:
            result['deposit_waive_amount'] = self.deposit_waive_amount
        if self.insurance_coverage is not None:
            result['insurance_coverage'] = self.insurance_coverage
        if self.insurance_order_no is not None:
            result['insurance_order_no'] = self.insurance_order_no
        if self.item_name is not None:
            result['item_name'] = self.item_name
        if self.item_price is not None:
            result['item_price'] = self.item_price
        if self.item_type is not None:
            result['item_type'] = self.item_type
        if self.merchant_alipay_account is not None:
            result['merchant_alipay_account'] = self.merchant_alipay_account
        if self.merchant_alipay_id is not None:
            result['merchant_alipay_id'] = self.merchant_alipay_id
        if self.merchant_name is not None:
            result['merchant_name'] = self.merchant_name
        if self.merchant_order_no is not None:
            result['merchant_order_no'] = self.merchant_order_no
        if self.payment_channel is not None:
            result['payment_channel'] = self.payment_channel
        if self.tenancy_term_end is not None:
            result['tenancy_term_end'] = self.tenancy_term_end
        if self.tenancy_term_start is not None:
            result['tenancy_term_start'] = self.tenancy_term_start
        if self.insured is not None:
            result['insured'] = self.insured
        if self.insurance_order_url is not None:
            result['insurance_order_url'] = self.insurance_order_url
        if self.insurance_bill_no is not None:
            result['insurance_bill_no'] = self.insurance_bill_no
        if self.insurance_bill_time is not None:
            result['insurance_bill_time'] = self.insurance_bill_time
        if self.insurance_bill_amount is not None:
            result['insurance_bill_amount'] = self.insurance_bill_amount
        if self.insurance_product_coverage is not None:
            result['insurance_product_coverage'] = self.insurance_product_coverage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('account_id') is not None:
            self.account_id = m.get('account_id')
        if m.get('alipay_order_amount') is not None:
            self.alipay_order_amount = m.get('alipay_order_amount')
        if m.get('alipay_order_no') is not None:
            self.alipay_order_no = m.get('alipay_order_no')
        if m.get('alipay_order_total_amount') is not None:
            self.alipay_order_total_amount = m.get('alipay_order_total_amount')
        if m.get('deposit_waive_amount') is not None:
            self.deposit_waive_amount = m.get('deposit_waive_amount')
        if m.get('insurance_coverage') is not None:
            self.insurance_coverage = m.get('insurance_coverage')
        if m.get('insurance_order_no') is not None:
            self.insurance_order_no = m.get('insurance_order_no')
        if m.get('item_name') is not None:
            self.item_name = m.get('item_name')
        if m.get('item_price') is not None:
            self.item_price = m.get('item_price')
        if m.get('item_type') is not None:
            self.item_type = m.get('item_type')
        if m.get('merchant_alipay_account') is not None:
            self.merchant_alipay_account = m.get('merchant_alipay_account')
        if m.get('merchant_alipay_id') is not None:
            self.merchant_alipay_id = m.get('merchant_alipay_id')
        if m.get('merchant_name') is not None:
            self.merchant_name = m.get('merchant_name')
        if m.get('merchant_order_no') is not None:
            self.merchant_order_no = m.get('merchant_order_no')
        if m.get('payment_channel') is not None:
            self.payment_channel = m.get('payment_channel')
        if m.get('tenancy_term_end') is not None:
            self.tenancy_term_end = m.get('tenancy_term_end')
        if m.get('tenancy_term_start') is not None:
            self.tenancy_term_start = m.get('tenancy_term_start')
        if m.get('insured') is not None:
            self.insured = m.get('insured')
        if m.get('insurance_order_url') is not None:
            self.insurance_order_url = m.get('insurance_order_url')
        if m.get('insurance_bill_no') is not None:
            self.insurance_bill_no = m.get('insurance_bill_no')
        if m.get('insurance_bill_time') is not None:
            self.insurance_bill_time = m.get('insurance_bill_time')
        if m.get('insurance_bill_amount') is not None:
            self.insurance_bill_amount = m.get('insurance_bill_amount')
        if m.get('insurance_product_coverage') is not None:
            self.insurance_product_coverage = m.get('insurance_product_coverage')
        return self


class CreateLeaseOrderResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 是否成功
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateNotarizationBillRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        alipay_order_no: str = None,
        alipay_uid: str = None,
        cert_name: str = None,
        cert_no: str = None,
        e_notarization_biz: str = None,
        e_notarization_download_url: str = None,
        e_notarization_no: str = None,
        e_notarization_page_no: str = None,
        e_notarization_status: str = None,
        e_notarization_usage: str = None,
        e_notarization_valid_date: str = None,
        legal_person_name: str = None,
        order_id: str = None,
        org_id: str = None,
        payment_amount: int = None,
        phone: str = None,
        scenario: str = None,
        user_type: int = None,
        fee_splitting: bool = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 支付宝交易订单号
        self.alipay_order_no = alipay_order_no
        # 支付宝用户ID
        self.alipay_uid = alipay_uid
        # 申请者名称
        self.cert_name = cert_name
        # 申请者证件号码：身份证号码（个人用户）或企业统一社会信用代码（企业用户）
        self.cert_no = cert_no
        # 电子公证书业务细项，如“200”对应出生公证
        self.e_notarization_biz = e_notarization_biz
        # 电子公证书下载地址
        self.e_notarization_download_url = e_notarization_download_url
        # 电子公证书编号
        self.e_notarization_no = e_notarization_no
        # 电子公证书页数
        self.e_notarization_page_no = e_notarization_page_no
        # 电子公证书状态码
        self.e_notarization_status = e_notarization_status
        # 电子公证书业务用途
        self.e_notarization_usage = e_notarization_usage
        # 电子公证书有效期
        self.e_notarization_valid_date = e_notarization_valid_date
        # 企业法人姓名（企业用户必填）
        self.legal_person_name = legal_person_name
        # 出证订单ID
        self.order_id = order_id
        # 出证机构ID
        self.org_id = org_id
        # 支付宝交易订单支付金额（人民币），单位为分
        self.payment_amount = payment_amount
        # 联系电话
        self.phone = phone
        # 场景枚举：E_NOTARIZATION（电子公证），NOTARY_CERTIFICATION（存证证明）
        self.scenario = scenario
        # 申请者身份类型，1个人，2企业
        self.user_type = user_type
        # 是否为酬金分润方式，是则按照订金额一定比例分润，否则直接支付订单金额
        self.fee_splitting = fee_splitting

    def validate(self):
        if self.e_notarization_valid_date is not None:
            self.validate_pattern(self.e_notarization_valid_date, 'e_notarization_valid_date', '\\d{4}[-]\\d{1,2}[-]\\d{1,2}[T]\\d{2}:\\d{2}:\\d{2}([Z]|([\\.]\\d{1,9})?[\\+]\\d{2}[\\:]?\\d{2})')
        self.validate_required(self.scenario, 'scenario')
        self.validate_required(self.fee_splitting, 'fee_splitting')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.alipay_order_no is not None:
            result['alipay_order_no'] = self.alipay_order_no
        if self.alipay_uid is not None:
            result['alipay_uid'] = self.alipay_uid
        if self.cert_name is not None:
            result['cert_name'] = self.cert_name
        if self.cert_no is not None:
            result['cert_no'] = self.cert_no
        if self.e_notarization_biz is not None:
            result['e_notarization_biz'] = self.e_notarization_biz
        if self.e_notarization_download_url is not None:
            result['e_notarization_download_url'] = self.e_notarization_download_url
        if self.e_notarization_no is not None:
            result['e_notarization_no'] = self.e_notarization_no
        if self.e_notarization_page_no is not None:
            result['e_notarization_page_no'] = self.e_notarization_page_no
        if self.e_notarization_status is not None:
            result['e_notarization_status'] = self.e_notarization_status
        if self.e_notarization_usage is not None:
            result['e_notarization_usage'] = self.e_notarization_usage
        if self.e_notarization_valid_date is not None:
            result['e_notarization_valid_date'] = self.e_notarization_valid_date
        if self.legal_person_name is not None:
            result['legal_person_name'] = self.legal_person_name
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.org_id is not None:
            result['org_id'] = self.org_id
        if self.payment_amount is not None:
            result['payment_amount'] = self.payment_amount
        if self.phone is not None:
            result['phone'] = self.phone
        if self.scenario is not None:
            result['scenario'] = self.scenario
        if self.user_type is not None:
            result['user_type'] = self.user_type
        if self.fee_splitting is not None:
            result['fee_splitting'] = self.fee_splitting
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('alipay_order_no') is not None:
            self.alipay_order_no = m.get('alipay_order_no')
        if m.get('alipay_uid') is not None:
            self.alipay_uid = m.get('alipay_uid')
        if m.get('cert_name') is not None:
            self.cert_name = m.get('cert_name')
        if m.get('cert_no') is not None:
            self.cert_no = m.get('cert_no')
        if m.get('e_notarization_biz') is not None:
            self.e_notarization_biz = m.get('e_notarization_biz')
        if m.get('e_notarization_download_url') is not None:
            self.e_notarization_download_url = m.get('e_notarization_download_url')
        if m.get('e_notarization_no') is not None:
            self.e_notarization_no = m.get('e_notarization_no')
        if m.get('e_notarization_page_no') is not None:
            self.e_notarization_page_no = m.get('e_notarization_page_no')
        if m.get('e_notarization_status') is not None:
            self.e_notarization_status = m.get('e_notarization_status')
        if m.get('e_notarization_usage') is not None:
            self.e_notarization_usage = m.get('e_notarization_usage')
        if m.get('e_notarization_valid_date') is not None:
            self.e_notarization_valid_date = m.get('e_notarization_valid_date')
        if m.get('legal_person_name') is not None:
            self.legal_person_name = m.get('legal_person_name')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('org_id') is not None:
            self.org_id = m.get('org_id')
        if m.get('payment_amount') is not None:
            self.payment_amount = m.get('payment_amount')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('scenario') is not None:
            self.scenario = m.get('scenario')
        if m.get('user_type') is not None:
            self.user_type = m.get('user_type')
        if m.get('fee_splitting') is not None:
            self.fee_splitting = m.get('fee_splitting')
        return self


class CreateNotarizationBillResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        accepted: bool = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 计费订单是否创建成功
        self.accepted = accepted

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.accepted is not None:
            result['accepted'] = self.accepted
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('accepted') is not None:
            self.accepted = m.get('accepted')
        return self


class InitCertificationRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        applier: Identity = None,
        notary_info: List[NotaryInfo] = None,
        type: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 申请人的身份信息
        self.applier = applier
        # 存证证明所要展示的存证信息，可填多个
        self.notary_info = notary_info
        # 存证证明的类型：STANDARD（标准存证证明）或COPYRIGHT（版权存证证明），默认为COPYRIGHT
        self.type = type

    def validate(self):
        self.validate_required(self.applier, 'applier')
        if self.applier:
            self.applier.validate()
        self.validate_required(self.notary_info, 'notary_info')
        if self.notary_info:
            for k in self.notary_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.applier is not None:
            result['applier'] = self.applier.to_map()
        result['notary_info'] = []
        if self.notary_info is not None:
            for k in self.notary_info:
                result['notary_info'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('applier') is not None:
            temp_model = Identity()
            self.applier = temp_model.from_map(m['applier'])
        self.notary_info = []
        if m.get('notary_info') is not None:
            for k in m.get('notary_info'):
                temp_model = NotaryInfo()
                self.notary_info.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class InitCertificationResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: str = None,
        message: str = None,
        order_id: str = None,
        pay_content: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 返回值状态码，0000则为成功
        self.code = code
        # 异常状态时的错误信息
        self.message = message
        # 后端生成的存证证明申请订单ID
        self.order_id = order_id
        # 如果是记账模式则为空，其余情况返回支付宝SDK生成的支付内容信息
        self.pay_content = pay_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.pay_content is not None:
            result['pay_content'] = self.pay_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('pay_content') is not None:
            self.pay_content = m.get('pay_content')
        return self


class QueryCertificationRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        order_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 存证证明申请的订单ID
        self.order_id = order_id

    def validate(self):
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.order_id is not None:
            result['order_id'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        return self


class QueryCertificationResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        certificate_info: List[CertificateInfo] = None,
        code: str = None,
        message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 存证证明的证书信息列表
        self.certificate_info = certificate_info
        # 返回值状态码，0000则为成功
        self.code = code
        # 异常状态时的错误信息
        self.message = message

    def validate(self):
        if self.certificate_info:
            for k in self.certificate_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        result['certificate_info'] = []
        if self.certificate_info is not None:
            for k in self.certificate_info:
                result['certificate_info'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        self.certificate_info = []
        if m.get('certificate_info') is not None:
            for k in m.get('certificate_info'):
                temp_model = CertificateInfo()
                self.certificate_info.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetTsrCertificateRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        return self


class GetTsrCertificateResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        return self


class SaveJointconstraintRecordRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        beneficiary_account_code: str = None,
        beneficiary_account_type: int = None,
        beneficiary_cert_number: str = None,
        beneficiary_cert_type: int = None,
        beneficiary_type: int = None,
        contract_code: str = None,
        contract_fulfillment_code: str = None,
        contract_name: str = None,
        contract_txhash: str = None,
        external_url: str = None,
        industry_code: str = None,
        paid_amount: str = None,
        paid_proof: str = None,
        paid_time: str = None,
        payer_account_code: str = None,
        payer_account_type: int = None,
        payer_cert_number: str = None,
        payer_cert_type: int = None,
        payer_type: int = None,
        payment_amount: str = None,
        payment_date_buffer: int = None,
        payment_deadline: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 收款账户
        self.beneficiary_account_code = beneficiary_account_code
        # 收款账户类型
        # 
        # 1：支付宝
        self.beneficiary_account_type = beneficiary_account_type
        # 应收方证件号码
        # 
        # 
        self.beneficiary_cert_number = beneficiary_cert_number
        # 应收方证件类型
        # 
        # 0：统一社会信用代码
        # 
        # 1：身份证号码
        self.beneficiary_cert_type = beneficiary_cert_type
        # 
        # 应收方类型
        # 
        # 0：企业
        # 
        # 1：个人
        self.beneficiary_type = beneficiary_type
        # 合同编号
        self.contract_code = contract_code
        # 合同履行记录标签
        self.contract_fulfillment_code = contract_fulfillment_code
        # 合同名称
        self.contract_name = contract_name
        # 合同存证哈希
        self.contract_txhash = contract_txhash
        # 商户端合同链接
        # 
        # 从智能合同小程序中跳转至商户端查看合同内容链接
        self.external_url = external_url
        # 所属行业，来自合同
        # 
        # 
        self.industry_code = industry_code
        # 已付金额
        # 
        # 
        self.paid_amount = paid_amount
        # 支付凭据
        # 
        # 
        self.paid_proof = paid_proof
        # 付款时间
        # 
        # 
        self.paid_time = paid_time
        # 付款账户
        # 
        # 
        self.payer_account_code = payer_account_code
        # 
        # 付款账户类型
        # 
        # 1：支付宝
        self.payer_account_type = payer_account_type
        # 应付方证件号码
        # 
        # 
        self.payer_cert_number = payer_cert_number
        # 应付方证件类型
        # 
        # 0：统一社会信用代码
        # 
        # 1：身份证号码
        self.payer_cert_type = payer_cert_type
        # 应付方类型
        # 
        # 0：企业
        # 
        # 1：个人
        self.payer_type = payer_type
        # 履约标的金额
        # 
        # 
        self.payment_amount = payment_amount
        # 履约宽限期，单位：天
        # 
        # 
        self.payment_date_buffer = payment_date_buffer
        # 目标履约日期
        # 
        # 
        self.payment_deadline = payment_deadline

    def validate(self):
        self.validate_required(self.beneficiary_cert_number, 'beneficiary_cert_number')
        self.validate_required(self.beneficiary_cert_type, 'beneficiary_cert_type')
        self.validate_required(self.beneficiary_type, 'beneficiary_type')
        self.validate_required(self.contract_code, 'contract_code')
        self.validate_required(self.contract_fulfillment_code, 'contract_fulfillment_code')
        self.validate_required(self.contract_name, 'contract_name')
        self.validate_required(self.contract_txhash, 'contract_txhash')
        if self.paid_time is not None:
            self.validate_pattern(self.paid_time, 'paid_time', '\\d{4}[-]\\d{1,2}[-]\\d{1,2}[T]\\d{2}:\\d{2}:\\d{2}([Z]|([\\.]\\d{1,9})?[\\+]\\d{2}[\\:]?\\d{2})')
        self.validate_required(self.payer_cert_number, 'payer_cert_number')
        self.validate_required(self.payer_cert_type, 'payer_cert_type')
        self.validate_required(self.payer_type, 'payer_type')
        self.validate_required(self.payment_amount, 'payment_amount')
        self.validate_required(self.payment_deadline, 'payment_deadline')
        if self.payment_deadline is not None:
            self.validate_pattern(self.payment_deadline, 'payment_deadline', '\\d{4}[-]\\d{1,2}[-]\\d{1,2}[T]\\d{2}:\\d{2}:\\d{2}([Z]|([\\.]\\d{1,9})?[\\+]\\d{2}[\\:]?\\d{2})')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.beneficiary_account_code is not None:
            result['beneficiary_account_code'] = self.beneficiary_account_code
        if self.beneficiary_account_type is not None:
            result['beneficiary_account_type'] = self.beneficiary_account_type
        if self.beneficiary_cert_number is not None:
            result['beneficiary_cert_number'] = self.beneficiary_cert_number
        if self.beneficiary_cert_type is not None:
            result['beneficiary_cert_type'] = self.beneficiary_cert_type
        if self.beneficiary_type is not None:
            result['beneficiary_type'] = self.beneficiary_type
        if self.contract_code is not None:
            result['contract_code'] = self.contract_code
        if self.contract_fulfillment_code is not None:
            result['contract_fulfillment_code'] = self.contract_fulfillment_code
        if self.contract_name is not None:
            result['contract_name'] = self.contract_name
        if self.contract_txhash is not None:
            result['contract_txhash'] = self.contract_txhash
        if self.external_url is not None:
            result['external_url'] = self.external_url
        if self.industry_code is not None:
            result['industry_code'] = self.industry_code
        if self.paid_amount is not None:
            result['paid_amount'] = self.paid_amount
        if self.paid_proof is not None:
            result['paid_proof'] = self.paid_proof
        if self.paid_time is not None:
            result['paid_time'] = self.paid_time
        if self.payer_account_code is not None:
            result['payer_account_code'] = self.payer_account_code
        if self.payer_account_type is not None:
            result['payer_account_type'] = self.payer_account_type
        if self.payer_cert_number is not None:
            result['payer_cert_number'] = self.payer_cert_number
        if self.payer_cert_type is not None:
            result['payer_cert_type'] = self.payer_cert_type
        if self.payer_type is not None:
            result['payer_type'] = self.payer_type
        if self.payment_amount is not None:
            result['payment_amount'] = self.payment_amount
        if self.payment_date_buffer is not None:
            result['payment_date_buffer'] = self.payment_date_buffer
        if self.payment_deadline is not None:
            result['payment_deadline'] = self.payment_deadline
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('beneficiary_account_code') is not None:
            self.beneficiary_account_code = m.get('beneficiary_account_code')
        if m.get('beneficiary_account_type') is not None:
            self.beneficiary_account_type = m.get('beneficiary_account_type')
        if m.get('beneficiary_cert_number') is not None:
            self.beneficiary_cert_number = m.get('beneficiary_cert_number')
        if m.get('beneficiary_cert_type') is not None:
            self.beneficiary_cert_type = m.get('beneficiary_cert_type')
        if m.get('beneficiary_type') is not None:
            self.beneficiary_type = m.get('beneficiary_type')
        if m.get('contract_code') is not None:
            self.contract_code = m.get('contract_code')
        if m.get('contract_fulfillment_code') is not None:
            self.contract_fulfillment_code = m.get('contract_fulfillment_code')
        if m.get('contract_name') is not None:
            self.contract_name = m.get('contract_name')
        if m.get('contract_txhash') is not None:
            self.contract_txhash = m.get('contract_txhash')
        if m.get('external_url') is not None:
            self.external_url = m.get('external_url')
        if m.get('industry_code') is not None:
            self.industry_code = m.get('industry_code')
        if m.get('paid_amount') is not None:
            self.paid_amount = m.get('paid_amount')
        if m.get('paid_proof') is not None:
            self.paid_proof = m.get('paid_proof')
        if m.get('paid_time') is not None:
            self.paid_time = m.get('paid_time')
        if m.get('payer_account_code') is not None:
            self.payer_account_code = m.get('payer_account_code')
        if m.get('payer_account_type') is not None:
            self.payer_account_type = m.get('payer_account_type')
        if m.get('payer_cert_number') is not None:
            self.payer_cert_number = m.get('payer_cert_number')
        if m.get('payer_cert_type') is not None:
            self.payer_cert_type = m.get('payer_cert_type')
        if m.get('payer_type') is not None:
            self.payer_type = m.get('payer_type')
        if m.get('payment_amount') is not None:
            self.payment_amount = m.get('payment_amount')
        if m.get('payment_date_buffer') is not None:
            self.payment_date_buffer = m.get('payment_date_buffer')
        if m.get('payment_deadline') is not None:
            self.payment_deadline = m.get('payment_deadline')
        return self


class SaveJointconstraintRecordResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        return self


class DeleteJointconstraintRecordRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        contract_code: str = None,
        contract_fulfillment_code: str = None,
        payer_cert_number: str = None,
        payer_cert_type: int = None,
        payer_type: int = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 合同编号
        # 
        # 
        self.contract_code = contract_code
        # 合同履行记录标签
        # 
        # 
        self.contract_fulfillment_code = contract_fulfillment_code
        # 应付方证件号码
        # 
        # 
        self.payer_cert_number = payer_cert_number
        # 应付方证件类型
        # 
        # 0：统一社会信用代码
        # 
        # 1：身份证号码
        self.payer_cert_type = payer_cert_type
        # 应付方类型
        # 
        # 0：企业
        # 
        # 1：个人
        self.payer_type = payer_type

    def validate(self):
        self.validate_required(self.contract_code, 'contract_code')
        self.validate_required(self.contract_fulfillment_code, 'contract_fulfillment_code')
        self.validate_required(self.payer_cert_number, 'payer_cert_number')
        self.validate_required(self.payer_cert_type, 'payer_cert_type')
        self.validate_required(self.payer_type, 'payer_type')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.contract_code is not None:
            result['contract_code'] = self.contract_code
        if self.contract_fulfillment_code is not None:
            result['contract_fulfillment_code'] = self.contract_fulfillment_code
        if self.payer_cert_number is not None:
            result['payer_cert_number'] = self.payer_cert_number
        if self.payer_cert_type is not None:
            result['payer_cert_type'] = self.payer_cert_type
        if self.payer_type is not None:
            result['payer_type'] = self.payer_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('contract_code') is not None:
            self.contract_code = m.get('contract_code')
        if m.get('contract_fulfillment_code') is not None:
            self.contract_fulfillment_code = m.get('contract_fulfillment_code')
        if m.get('payer_cert_number') is not None:
            self.payer_cert_number = m.get('payer_cert_number')
        if m.get('payer_cert_type') is not None:
            self.payer_cert_type = m.get('payer_cert_type')
        if m.get('payer_type') is not None:
            self.payer_type = m.get('payer_type')
        return self


class DeleteJointconstraintRecordResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        return self


class QueryJointconstraintBreachrecordRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        entity_type: int = None,
        cert_type: int = None,
        cert_number: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 查询对象实体类型
        # 
        # 0：企业
        # 
        # 1：个人
        self.entity_type = entity_type
        # 对象实体证件类型
        # 
        # 0：统一社会信用代码
        # 
        # 1：身份证号码
        self.cert_type = cert_type
        # 对象实体证件号码
        # 
        # 
        self.cert_number = cert_number

    def validate(self):
        self.validate_required(self.entity_type, 'entity_type')
        self.validate_required(self.cert_type, 'cert_type')
        self.validate_required(self.cert_number, 'cert_number')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.entity_type is not None:
            result['entity_type'] = self.entity_type
        if self.cert_type is not None:
            result['cert_type'] = self.cert_type
        if self.cert_number is not None:
            result['cert_number'] = self.cert_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('entity_type') is not None:
            self.entity_type = m.get('entity_type')
        if m.get('cert_type') is not None:
            self.cert_type = m.get('cert_type')
        if m.get('cert_number') is not None:
            self.cert_number = m.get('cert_number')
        return self


class QueryJointconstraintBreachrecordResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        has_record: bool = None,
        breach_count: int = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 是否存在履行记录
        # 
        # 
        self.has_record = has_record
        # 违约次数
        # 
        # 
        self.breach_count = breach_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.has_record is not None:
            result['has_record'] = self.has_record
        if self.breach_count is not None:
            result['breach_count'] = self.breach_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('has_record') is not None:
            self.has_record = m.get('has_record')
        if m.get('breach_count') is not None:
            self.breach_count = m.get('breach_count')
        return self


class ApplyJusticeMediationRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        product_code: str = None,
        court_code: str = None,
        case_body: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 机构码 由蚂蚁分配
        self.product_code = product_code
        # 法院代码 由蚂蚁提供
        self.court_code = court_code
        # 案件内容 JsonString 格式{"agencyRelations":[],"agents":[],"caseInfo":{},"litigants":{}}
        self.case_body = case_body

    def validate(self):
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.court_code, 'court_code')
        self.validate_required(self.case_body, 'case_body')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.product_code is not None:
            result['product_code'] = self.product_code
        if self.court_code is not None:
            result['court_code'] = self.court_code
        if self.case_body is not None:
            result['case_body'] = self.case_body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('product_code') is not None:
            self.product_code = m.get('product_code')
        if m.get('court_code') is not None:
            self.court_code = m.get('court_code')
        if m.get('case_body') is not None:
            self.case_body = m.get('case_body')
        return self


class ApplyJusticeMediationResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class QueryJusticeMediationRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        product_code: str = None,
        case_number: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 产品码 由蚂蚁分配
        # 
        self.product_code = product_code
        # 案件编号
        self.case_number = case_number

    def validate(self):
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.case_number, 'case_number')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.product_code is not None:
            result['product_code'] = self.product_code
        if self.case_number is not None:
            result['case_number'] = self.case_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('product_code') is not None:
            self.product_code = m.get('product_code')
        if m.get('case_number') is not None:
            self.case_number = m.get('case_number')
        return self


class QueryJusticeMediationResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        mediation_case_detail_info: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务码，0表示成功
        self.code = code
        # 业务码信息
        self.message = message
        # 案件处理进度信息对象
        self.mediation_case_detail_info = mediation_case_detail_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.mediation_case_detail_info is not None:
            result['mediation_case_detail_info'] = self.mediation_case_detail_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('mediation_case_detail_info') is not None:
            self.mediation_case_detail_info = m.get('mediation_case_detail_info')
        return self


class CreateWitnessFlowRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        business_scene: str = None,
        client_name: str = None,
        client_version: str = None,
        contract_validity: str = None,
        flow_id: str = None,
        initiator_account_id: str = None,
        launch_endpoint: str = None,
        launch_ip: str = None,
        mobile_shield_version: int = None,
        payer_account_id: str = None,
        sign_deadline: str = None,
        sign_order: str = None,
        type: int = None,
        app_id: str = None,
        token: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 业务场景，最大255长度
        self.business_scene = business_scene
        # 客户端名称，比如签章客户端，最长长度50
        self.client_name = client_name
        # 客户端版本
        self.client_version = client_version
        # 合同有效截止时间，时间戳
        self.contract_validity = contract_validity
        # 流程id
        self.flow_id = flow_id
        # 发起方账号id
        self.initiator_account_id = initiator_account_id
        # 发起端，TIANYIN_H5 - H5端，TIANYIN_WEB - WEB端，TIANYIN_API - API
        self.launch_endpoint = launch_endpoint
        # 发起ip
        self.launch_ip = launch_ip
        # 手机盾逻辑版本，0-不支持用印审批、需要扣费，1-支持用印审批、无需扣费，默认0
        self.mobile_shield_version = mobile_shield_version
        # 扣费方账号id
        self.payer_account_id = payer_account_id
        # 签署截止时间，时间戳
        self.sign_deadline = sign_deadline
        # 签署顺序，SIGN_SEQUENCE-顺序签署，SIGN_NON_SEQUENCE-无序签署
        self.sign_order = sign_order
        # 流程类型，0-签署流程，1-作废流程，默认0
        self.type = type
        # 发起请求的实例应用ID
        self.app_id = app_id
        # 发起请求的鉴权token
        self.token = token

    def validate(self):
        self.validate_required(self.business_scene, 'business_scene')
        self.validate_required(self.launch_endpoint, 'launch_endpoint')
        self.validate_required(self.launch_ip, 'launch_ip')
        self.validate_required(self.sign_order, 'sign_order')
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.token, 'token')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.business_scene is not None:
            result['business_scene'] = self.business_scene
        if self.client_name is not None:
            result['client_name'] = self.client_name
        if self.client_version is not None:
            result['client_version'] = self.client_version
        if self.contract_validity is not None:
            result['contract_validity'] = self.contract_validity
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.initiator_account_id is not None:
            result['initiator_account_id'] = self.initiator_account_id
        if self.launch_endpoint is not None:
            result['launch_endpoint'] = self.launch_endpoint
        if self.launch_ip is not None:
            result['launch_ip'] = self.launch_ip
        if self.mobile_shield_version is not None:
            result['mobile_shield_version'] = self.mobile_shield_version
        if self.payer_account_id is not None:
            result['payer_account_id'] = self.payer_account_id
        if self.sign_deadline is not None:
            result['sign_deadline'] = self.sign_deadline
        if self.sign_order is not None:
            result['sign_order'] = self.sign_order
        if self.type is not None:
            result['type'] = self.type
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('business_scene') is not None:
            self.business_scene = m.get('business_scene')
        if m.get('client_name') is not None:
            self.client_name = m.get('client_name')
        if m.get('client_version') is not None:
            self.client_version = m.get('client_version')
        if m.get('contract_validity') is not None:
            self.contract_validity = m.get('contract_validity')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('initiator_account_id') is not None:
            self.initiator_account_id = m.get('initiator_account_id')
        if m.get('launch_endpoint') is not None:
            self.launch_endpoint = m.get('launch_endpoint')
        if m.get('launch_ip') is not None:
            self.launch_ip = m.get('launch_ip')
        if m.get('mobile_shield_version') is not None:
            self.mobile_shield_version = m.get('mobile_shield_version')
        if m.get('payer_account_id') is not None:
            self.payer_account_id = m.get('payer_account_id')
        if m.get('sign_deadline') is not None:
            self.sign_deadline = m.get('sign_deadline')
        if m.get('sign_order') is not None:
            self.sign_order = m.get('sign_order')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class CreateWitnessFlowResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        flow_config: WitnessFlowConfig = None,
        message: str = None,
        witness_flow_id: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 错误码
        self.code = code
        # 流程配置
        self.flow_config = flow_config
        # 流程创建响应数据
        self.message = message
        # 见证流程
        self.witness_flow_id = witness_flow_id

    def validate(self):
        if self.flow_config:
            self.flow_config.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.flow_config is not None:
            result['flow_config'] = self.flow_config.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.witness_flow_id is not None:
            result['witness_flow_id'] = self.witness_flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('flow_config') is not None:
            temp_model = WitnessFlowConfig()
            self.flow_config = temp_model.from_map(m['flow_config'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('witness_flow_id') is not None:
            self.witness_flow_id = m.get('witness_flow_id')
        return self


class SaveWitnessSnapshotRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        data: str = None,
        step: str = None,
        step_description: str = None,
        witness_flow_id: str = None,
        app_id: str = None,
        token: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 快照数据
        self.data = data
        # 快照步骤，最大20长度，START-开始，UPDATE-更新，FINISH-结束，允许自定义
        self.step = step
        # 快照步骤描述，最大40长度
        self.step_description = step_description
        # 见证流程id
        self.witness_flow_id = witness_flow_id
        # 发起请求的实例应用ID
        self.app_id = app_id
        # 发起请求的鉴权token
        self.token = token

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.step, 'step')
        self.validate_required(self.step_description, 'step_description')
        self.validate_required(self.witness_flow_id, 'witness_flow_id')
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.token, 'token')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.data is not None:
            result['data'] = self.data
        if self.step is not None:
            result['step'] = self.step
        if self.step_description is not None:
            result['step_description'] = self.step_description
        if self.witness_flow_id is not None:
            result['witness_flow_id'] = self.witness_flow_id
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('step') is not None:
            self.step = m.get('step')
        if m.get('step_description') is not None:
            self.step_description = m.get('step_description')
        if m.get('witness_flow_id') is not None:
            self.witness_flow_id = m.get('witness_flow_id')
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class SaveWitnessSnapshotResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 错误码
        self.code = code
        # 错误信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CheckWitnessSignaccessRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        approval_flow_id: str = None,
        approval_notify_url: str = None,
        docs: List[WitnessDocs] = None,
        endpoint: str = None,
        launch_approval: bool = None,
        mobile_shield_task_id: str = None,
        realname_auth_code: str = None,
        seal_ids: List[str] = None,
        signer_account_id: str = None,
        signer_ip: str = None,
        signer_type: int = None,
        sign_preview_url: str = None,
        will_auth_code: str = None,
        witness_flow_id: str = None,
        app_id: str = None,
        token: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 审批流程id
        self.approval_flow_id = approval_flow_id
        # 审批结果通知
        self.approval_notify_url = approval_notify_url
        # 签署文档信息
        self.docs = docs
        # 签署端，TIANYIN_H5 - H5端，TIANYIN_WEB - WEB端，TIANYIN_API - API
        self.endpoint = endpoint
        # 是否发起审批，默认TRUE
        self.launch_approval = launch_approval
        # 手机盾任务id，用于手机盾审批场景
        self.mobile_shield_task_id = mobile_shield_task_id
        # 实名认证凭证
        self.realname_auth_code = realname_auth_code
        # 印章id列表
        self.seal_ids = seal_ids
        # 签署人账号id
        self.signer_account_id = signer_account_id
        # 签署人ip
        self.signer_ip = signer_ip
        # 签署人类型，1-私有云用户，2-公有云用户，3-手机盾用户
        self.signer_type = signer_type
        # 签署预览地址
        self.sign_preview_url = sign_preview_url
        # 意愿认证凭证
        self.will_auth_code = will_auth_code
        # 见证流程id
        self.witness_flow_id = witness_flow_id
        # 发起请求的实例应用ID
        self.app_id = app_id
        # 发起请求的鉴权token
        self.token = token

    def validate(self):
        self.validate_required(self.docs, 'docs')
        if self.docs:
            for k in self.docs:
                if k:
                    k.validate()
        self.validate_required(self.endpoint, 'endpoint')
        self.validate_required(self.signer_account_id, 'signer_account_id')
        self.validate_required(self.signer_ip, 'signer_ip')
        self.validate_required(self.signer_type, 'signer_type')
        self.validate_required(self.witness_flow_id, 'witness_flow_id')
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.token, 'token')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.approval_flow_id is not None:
            result['approval_flow_id'] = self.approval_flow_id
        if self.approval_notify_url is not None:
            result['approval_notify_url'] = self.approval_notify_url
        result['docs'] = []
        if self.docs is not None:
            for k in self.docs:
                result['docs'].append(k.to_map() if k else None)
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.launch_approval is not None:
            result['launch_approval'] = self.launch_approval
        if self.mobile_shield_task_id is not None:
            result['mobile_shield_task_id'] = self.mobile_shield_task_id
        if self.realname_auth_code is not None:
            result['realname_auth_code'] = self.realname_auth_code
        if self.seal_ids is not None:
            result['seal_ids'] = self.seal_ids
        if self.signer_account_id is not None:
            result['signer_account_id'] = self.signer_account_id
        if self.signer_ip is not None:
            result['signer_ip'] = self.signer_ip
        if self.signer_type is not None:
            result['signer_type'] = self.signer_type
        if self.sign_preview_url is not None:
            result['sign_preview_url'] = self.sign_preview_url
        if self.will_auth_code is not None:
            result['will_auth_code'] = self.will_auth_code
        if self.witness_flow_id is not None:
            result['witness_flow_id'] = self.witness_flow_id
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('approval_flow_id') is not None:
            self.approval_flow_id = m.get('approval_flow_id')
        if m.get('approval_notify_url') is not None:
            self.approval_notify_url = m.get('approval_notify_url')
        self.docs = []
        if m.get('docs') is not None:
            for k in m.get('docs'):
                temp_model = WitnessDocs()
                self.docs.append(temp_model.from_map(k))
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('launch_approval') is not None:
            self.launch_approval = m.get('launch_approval')
        if m.get('mobile_shield_task_id') is not None:
            self.mobile_shield_task_id = m.get('mobile_shield_task_id')
        if m.get('realname_auth_code') is not None:
            self.realname_auth_code = m.get('realname_auth_code')
        if m.get('seal_ids') is not None:
            self.seal_ids = m.get('seal_ids')
        if m.get('signer_account_id') is not None:
            self.signer_account_id = m.get('signer_account_id')
        if m.get('signer_ip') is not None:
            self.signer_ip = m.get('signer_ip')
        if m.get('signer_type') is not None:
            self.signer_type = m.get('signer_type')
        if m.get('sign_preview_url') is not None:
            self.sign_preview_url = m.get('sign_preview_url')
        if m.get('will_auth_code') is not None:
            self.will_auth_code = m.get('will_auth_code')
        if m.get('witness_flow_id') is not None:
            self.witness_flow_id = m.get('witness_flow_id')
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class CheckWitnessSignaccessResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        access_seal_ids: List[str] = None,
        approval_datas: List[WitnessApprovalData] = None,
        code: int = None,
        message: str = None,
        sign_ticket: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 有权限的印章id列表
        self.access_seal_ids = access_seal_ids
        # 审批数据
        self.approval_datas = approval_datas
        # 错误码
        self.code = code
        # 错误信息
        self.message = message
        # 签署票证
        self.sign_ticket = sign_ticket

    def validate(self):
        if self.approval_datas:
            for k in self.approval_datas:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.access_seal_ids is not None:
            result['access_seal_ids'] = self.access_seal_ids
        result['approval_datas'] = []
        if self.approval_datas is not None:
            for k in self.approval_datas:
                result['approval_datas'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.sign_ticket is not None:
            result['sign_ticket'] = self.sign_ticket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('access_seal_ids') is not None:
            self.access_seal_ids = m.get('access_seal_ids')
        self.approval_datas = []
        if m.get('approval_datas') is not None:
            for k in m.get('approval_datas'):
                temp_model = WitnessApprovalData()
                self.approval_datas.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('sign_ticket') is not None:
            self.sign_ticket = m.get('sign_ticket')
        return self


class AuthWitnessFlowRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        app_id: str = None,
        cert_id: str = None,
        page: str = None,
        pos_x: str = None,
        pos_y: str = None,
        seal_file_key: str = None,
        seal_id: str = None,
        seal_type: int = None,
        signature_type: str = None,
        sign_datas: str = None,
        sign_hash: str = None,
        sign_ticket: str = None,
        subject_account_id: str = None,
        third_doc_id: str = None,
        token: str = None,
        witness_flow_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 发起请求的实例应用ID
        self.app_id = app_id
        # 证书id
        self.cert_id = cert_id
        # 签署页码，单个签时必传
        self.page = page
        # 签署x坐标，单个签时必传
        self.pos_x = pos_x
        # 签署y坐标，单个签时必传
        self.pos_y = pos_y
        # 印章图片key
        self.seal_file_key = seal_file_key
        # 印章id
        self.seal_id = seal_id
        # 印章类型，1-模板，2-手绘
        self.seal_type = seal_type
        # 签署类型，单个签时必传
        self.signature_type = signature_type
        # 批量签署信息，批量签时必传
        self.sign_datas = sign_datas
        # 待签署文档摘要值，单个签时必传
        self.sign_hash = sign_hash
        # 签署票证
        self.sign_ticket = sign_ticket
        # 签署主体账号id
        self.subject_account_id = subject_account_id
        # 第三方文档id，单个签时必传
        self.third_doc_id = third_doc_id
        # 发起请求的鉴权token
        self.token = token
        # 见证流程id
        self.witness_flow_id = witness_flow_id

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.seal_type, 'seal_type')
        self.validate_required(self.sign_ticket, 'sign_ticket')
        self.validate_required(self.token, 'token')
        self.validate_required(self.witness_flow_id, 'witness_flow_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.cert_id is not None:
            result['cert_id'] = self.cert_id
        if self.page is not None:
            result['page'] = self.page
        if self.pos_x is not None:
            result['pos_x'] = self.pos_x
        if self.pos_y is not None:
            result['pos_y'] = self.pos_y
        if self.seal_file_key is not None:
            result['seal_file_key'] = self.seal_file_key
        if self.seal_id is not None:
            result['seal_id'] = self.seal_id
        if self.seal_type is not None:
            result['seal_type'] = self.seal_type
        if self.signature_type is not None:
            result['signature_type'] = self.signature_type
        if self.sign_datas is not None:
            result['sign_datas'] = self.sign_datas
        if self.sign_hash is not None:
            result['sign_hash'] = self.sign_hash
        if self.sign_ticket is not None:
            result['sign_ticket'] = self.sign_ticket
        if self.subject_account_id is not None:
            result['subject_account_id'] = self.subject_account_id
        if self.third_doc_id is not None:
            result['third_doc_id'] = self.third_doc_id
        if self.token is not None:
            result['token'] = self.token
        if self.witness_flow_id is not None:
            result['witness_flow_id'] = self.witness_flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        if m.get('cert_id') is not None:
            self.cert_id = m.get('cert_id')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pos_x') is not None:
            self.pos_x = m.get('pos_x')
        if m.get('pos_y') is not None:
            self.pos_y = m.get('pos_y')
        if m.get('seal_file_key') is not None:
            self.seal_file_key = m.get('seal_file_key')
        if m.get('seal_id') is not None:
            self.seal_id = m.get('seal_id')
        if m.get('seal_type') is not None:
            self.seal_type = m.get('seal_type')
        if m.get('signature_type') is not None:
            self.signature_type = m.get('signature_type')
        if m.get('sign_datas') is not None:
            self.sign_datas = m.get('sign_datas')
        if m.get('sign_hash') is not None:
            self.sign_hash = m.get('sign_hash')
        if m.get('sign_ticket') is not None:
            self.sign_ticket = m.get('sign_ticket')
        if m.get('subject_account_id') is not None:
            self.subject_account_id = m.get('subject_account_id')
        if m.get('third_doc_id') is not None:
            self.third_doc_id = m.get('third_doc_id')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('witness_flow_id') is not None:
            self.witness_flow_id = m.get('witness_flow_id')
        return self


class AuthWitnessFlowResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
        qrcode_content: str = None,
        signlog_id: str = None,
        sign_result: str = None,
        sign_results: List[WitnessSignResult] = None,
        sign_way: int = None,
        task_id: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 错误码
        self.code = code
        # 错误信息
        self.message = message
        # 二维码内容
        self.qrcode_content = qrcode_content
        # 签署日志id，外部用户签署返回
        self.signlog_id = signlog_id
        # 签名结果，外部用户签署返回
        self.sign_result = sign_result
        # 签署结果，批量签署返回
        self.sign_results = sign_results
        # 签署方式，1-单个签署，2-批量签署
        self.sign_way = sign_way
        # 手机盾用户签署返回
        self.task_id = task_id

    def validate(self):
        if self.sign_results:
            for k in self.sign_results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.qrcode_content is not None:
            result['qrcode_content'] = self.qrcode_content
        if self.signlog_id is not None:
            result['signlog_id'] = self.signlog_id
        if self.sign_result is not None:
            result['sign_result'] = self.sign_result
        result['sign_results'] = []
        if self.sign_results is not None:
            for k in self.sign_results:
                result['sign_results'].append(k.to_map() if k else None)
        if self.sign_way is not None:
            result['sign_way'] = self.sign_way
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('qrcode_content') is not None:
            self.qrcode_content = m.get('qrcode_content')
        if m.get('signlog_id') is not None:
            self.signlog_id = m.get('signlog_id')
        if m.get('sign_result') is not None:
            self.sign_result = m.get('sign_result')
        self.sign_results = []
        if m.get('sign_results') is not None:
            for k in m.get('sign_results'):
                temp_model = WitnessSignResult()
                self.sign_results.append(temp_model.from_map(k))
        if m.get('sign_way') is not None:
            self.sign_way = m.get('sign_way')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class ConfirmWitnessFlowRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        confirm_datas: List[WitnessConfirmData] = None,
        evidence_ids: List[str] = None,
        signlog_ids: List[str] = None,
        sign_ticket: str = None,
        witness_flow_id: str = None,
        app_id: str = None,
        token: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 签署确认数据
        self.confirm_datas = confirm_datas
        # 证据id列表，内部用户必传
        self.evidence_ids = evidence_ids
        # 签署记录id列表，外部用户必传
        self.signlog_ids = signlog_ids
        # 签署票证
        self.sign_ticket = sign_ticket
        # 见证流程id
        self.witness_flow_id = witness_flow_id
        # 发起请求的实例应用ID
        self.app_id = app_id
        # 发起请求的鉴权token
        self.token = token

    def validate(self):
        self.validate_required(self.confirm_datas, 'confirm_datas')
        if self.confirm_datas:
            for k in self.confirm_datas:
                if k:
                    k.validate()
        self.validate_required(self.sign_ticket, 'sign_ticket')
        self.validate_required(self.witness_flow_id, 'witness_flow_id')
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.token, 'token')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        result['confirm_datas'] = []
        if self.confirm_datas is not None:
            for k in self.confirm_datas:
                result['confirm_datas'].append(k.to_map() if k else None)
        if self.evidence_ids is not None:
            result['evidence_ids'] = self.evidence_ids
        if self.signlog_ids is not None:
            result['signlog_ids'] = self.signlog_ids
        if self.sign_ticket is not None:
            result['sign_ticket'] = self.sign_ticket
        if self.witness_flow_id is not None:
            result['witness_flow_id'] = self.witness_flow_id
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        self.confirm_datas = []
        if m.get('confirm_datas') is not None:
            for k in m.get('confirm_datas'):
                temp_model = WitnessConfirmData()
                self.confirm_datas.append(temp_model.from_map(k))
        if m.get('evidence_ids') is not None:
            self.evidence_ids = m.get('evidence_ids')
        if m.get('signlog_ids') is not None:
            self.signlog_ids = m.get('signlog_ids')
        if m.get('sign_ticket') is not None:
            self.sign_ticket = m.get('sign_ticket')
        if m.get('witness_flow_id') is not None:
            self.witness_flow_id = m.get('witness_flow_id')
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class ConfirmWitnessFlowResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 错误码
        self.code = code
        # 错误信息
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateTransRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        customer: Identity = None,
        properties: str = None,
        sub_biz_id: str = None,
        tsr: bool = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 存证关联实体（个人/企业）的身份识别信息
        self.customer = customer
        # 扩展属性
        self.properties = properties
        # 业务子类型标识
        self.sub_biz_id = sub_biz_id
        # 是否使用可信时间戳，默认为false
        self.tsr = tsr

    def validate(self):
        self.validate_required(self.customer, 'customer')
        if self.customer:
            self.customer.validate()

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.customer is not None:
            result['customer'] = self.customer.to_map()
        if self.properties is not None:
            result['properties'] = self.properties
        if self.sub_biz_id is not None:
            result['sub_biz_id'] = self.sub_biz_id
        if self.tsr is not None:
            result['tsr'] = self.tsr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('customer') is not None:
            temp_model = Identity()
            self.customer = temp_model.from_map(m['customer'])
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('sub_biz_id') is not None:
            self.sub_biz_id = m.get('sub_biz_id')
        if m.get('tsr') is not None:
            self.tsr = m.get('tsr')
        return self


class CreateTransResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        transaction_id: str = None,
        tsr: TsrResponse = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 返回事务ID，全局唯一
        self.transaction_id = transaction_id
        # 可信时间信息
        self.tsr = tsr

    def validate(self):
        if self.tsr:
            self.tsr.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.tsr is not None:
            result['tsr'] = self.tsr.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('tsr') is not None:
            temp_model = TsrResponse()
            self.tsr = temp_model.from_map(m['tsr'])
        return self


class GetTransRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        transaction_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 存证事务ID
        self.transaction_id = transaction_id

    def validate(self):
        self.validate_required(self.transaction_id, 'transaction_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        return self


class GetTransResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        file_url: List[str] = None,
        transaction_id: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 返回文件下载路径列表
        self.file_url = file_url
        # 存证事务ID
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.file_url is not None:
            result['file_url'] = self.file_url
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('file_url') is not None:
            self.file_url = m.get('file_url')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        return self


class CreateTextRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        location: Location = None,
        notary_content: str = None,
        phase: str = None,
        properties: str = None,
        transaction_id: str = None,
        tsr: bool = None,
        text_notary_type: str = None,
        hash_algorithm: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 存证地点(如手机硬件ID，Wi-Fi地址，GPS位置，IP地址)
        self.location = location
        # 存证内容
        self.notary_content = notary_content
        # 描述本条存证在存证事务中的阶段，用户可自行维护
        self.phase = phase
        # 扩展属性
        self.properties = properties
        # 存证事务id
        self.transaction_id = transaction_id
        # 是否使用可信时间戳，默认为false
        self.tsr = tsr
        # 文本存证类型，支持源文本/文本哈希
        self.text_notary_type = text_notary_type
        # 哈希算法，目前仅支持 SHA256
        self.hash_algorithm = hash_algorithm

    def validate(self):
        if self.location:
            self.location.validate()
        self.validate_required(self.notary_content, 'notary_content')
        self.validate_required(self.phase, 'phase')
        self.validate_required(self.transaction_id, 'transaction_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.notary_content is not None:
            result['notary_content'] = self.notary_content
        if self.phase is not None:
            result['phase'] = self.phase
        if self.properties is not None:
            result['properties'] = self.properties
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.tsr is not None:
            result['tsr'] = self.tsr
        if self.text_notary_type is not None:
            result['text_notary_type'] = self.text_notary_type
        if self.hash_algorithm is not None:
            result['hash_algorithm'] = self.hash_algorithm
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('location') is not None:
            temp_model = Location()
            self.location = temp_model.from_map(m['location'])
        if m.get('notary_content') is not None:
            self.notary_content = m.get('notary_content')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('tsr') is not None:
            self.tsr = m.get('tsr')
        if m.get('text_notary_type') is not None:
            self.text_notary_type = m.get('text_notary_type')
        if m.get('hash_algorithm') is not None:
            self.hash_algorithm = m.get('hash_algorithm')
        return self


class CreateTextResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        tsr: TsrResponse = None,
        tx_hash: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 可信时间信息
        self.tsr = tsr
        # 存证凭据
        self.tx_hash = tx_hash

    def validate(self):
        if self.tsr:
            self.tsr.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.tsr is not None:
            result['tsr'] = self.tsr.to_map()
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('tsr') is not None:
            temp_model = TsrResponse()
            self.tsr = temp_model.from_map(m['tsr'])
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class GetTextRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        location: Location = None,
        phase: str = None,
        properties: str = None,
        transaction_id: str = None,
        tx_hash: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 存证地点(如手机硬件ID，Wi-Fi地址，GPS位置，IP地址)
        self.location = location
        # 描述本条存证在存证事务中的阶段，用户可自行维护
        self.phase = phase
        # 扩展属性
        self.properties = properties
        # 存证事务id
        self.transaction_id = transaction_id
        # 存证凭据
        self.tx_hash = tx_hash

    def validate(self):
        if self.location:
            self.location.validate()
        self.validate_required(self.tx_hash, 'tx_hash')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.properties is not None:
            result['properties'] = self.properties
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('location') is not None:
            temp_model = Location()
            self.location = temp_model.from_map(m['location'])
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class GetTextResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        content: str = None,
        tsr: TsrResponse = None,
        text_notary_type: str = None,
        hash_algorithm: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 存证信息
        self.content = content
        # 可信信息
        self.tsr = tsr
        # 文本存证类型
        self.text_notary_type = text_notary_type
        # 哈希算法
        self.hash_algorithm = hash_algorithm

    def validate(self):
        if self.tsr:
            self.tsr.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.content is not None:
            result['content'] = self.content
        if self.tsr is not None:
            result['tsr'] = self.tsr.to_map()
        if self.text_notary_type is not None:
            result['text_notary_type'] = self.text_notary_type
        if self.hash_algorithm is not None:
            result['hash_algorithm'] = self.hash_algorithm
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('tsr') is not None:
            temp_model = TsrResponse()
            self.tsr = temp_model.from_map(m['tsr'])
        if m.get('text_notary_type') is not None:
            self.text_notary_type = m.get('text_notary_type')
        if m.get('hash_algorithm') is not None:
            self.hash_algorithm = m.get('hash_algorithm')
        return self


class CreateFileRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        file_notary_type: str = None,
        hash_algorithm: str = None,
        location: Location = None,
        notary_file: str = None,
        notary_name: str = None,
        phase: str = None,
        properties: str = None,
        transaction_id: str = None,
        tsr: bool = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 文件存证模式，目前仅支持 FILE_RAW 和 FILE_HASH
        self.file_notary_type = file_notary_type
        # 当文件存证模式为FILE_HASH时，用户可以指定该参数。当前服务仅支持 SHA256，若不填写，则默认值为 SHA256。
        self.hash_algorithm = hash_algorithm
        # 存证地点(如手机硬件ID，Wi-Fi地址，GPS位置，IP地址)
        self.location = location
        # 存证文件内容，对文件内容做base64编码后得到。例如FILE_RAW模式下，文件内容为“test”，那么base64编码后的结果则为“dGVzdA==”。如果是FILE_HASh模式，则该字段直接为文件hash。
        self.notary_file = notary_file
        # 存证文件名称
        self.notary_name = notary_name
        # 描述本条存证在存证事务中的阶段，用户可自行维护
        self.phase = phase
        # 扩展属性
        self.properties = properties
        # 存证事务ID
        self.transaction_id = transaction_id
        # 是否使用可信时间戳，默认为false
        self.tsr = tsr

    def validate(self):
        if self.location:
            self.location.validate()
        self.validate_required(self.notary_file, 'notary_file')
        self.validate_required(self.notary_name, 'notary_name')
        self.validate_required(self.phase, 'phase')
        self.validate_required(self.transaction_id, 'transaction_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.file_notary_type is not None:
            result['file_notary_type'] = self.file_notary_type
        if self.hash_algorithm is not None:
            result['hash_algorithm'] = self.hash_algorithm
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.notary_file is not None:
            result['notary_file'] = self.notary_file
        if self.notary_name is not None:
            result['notary_name'] = self.notary_name
        if self.phase is not None:
            result['phase'] = self.phase
        if self.properties is not None:
            result['properties'] = self.properties
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.tsr is not None:
            result['tsr'] = self.tsr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('file_notary_type') is not None:
            self.file_notary_type = m.get('file_notary_type')
        if m.get('hash_algorithm') is not None:
            self.hash_algorithm = m.get('hash_algorithm')
        if m.get('location') is not None:
            temp_model = Location()
            self.location = temp_model.from_map(m['location'])
        if m.get('notary_file') is not None:
            self.notary_file = m.get('notary_file')
        if m.get('notary_name') is not None:
            self.notary_name = m.get('notary_name')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('tsr') is not None:
            self.tsr = m.get('tsr')
        return self


class CreateFileResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        tsr: TsrResponse = None,
        tx_hash: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 可信时间信息
        self.tsr = tsr
        # 存证凭证
        self.tx_hash = tx_hash

    def validate(self):
        if self.tsr:
            self.tsr.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.tsr is not None:
            result['tsr'] = self.tsr.to_map()
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('tsr') is not None:
            temp_model = TsrResponse()
            self.tsr = temp_model.from_map(m['tsr'])
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class GetFileRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        location: Location = None,
        phase: str = None,
        properties: str = None,
        transaction_id: str = None,
        tx_hash: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 存证地点(如手机硬件ID，Wi-Fi地址，GPS位置，IP地址)
        self.location = location
        # 描述本条存证在存证事务中的阶段，用户可自行维护
        self.phase = phase
        # 扩展属性
        self.properties = properties
        # 存证事务ID
        self.transaction_id = transaction_id
        # 存证凭据
        self.tx_hash = tx_hash

    def validate(self):
        if self.location:
            self.location.validate()
        self.validate_required(self.tx_hash, 'tx_hash')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.properties is not None:
            result['properties'] = self.properties
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('location') is not None:
            temp_model = Location()
            self.location = temp_model.from_map(m['location'])
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class GetFileResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        file_hash: str = None,
        file_notary_type: str = None,
        hash_algorithm: str = None,
        oss_path: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 文件哈希，当 file_notary_type 为 FILE_HASH 时才有此值。
        self.file_hash = file_hash
        # 文件存证模式，有 FILE_RAW 和 FILE_HASH 两种可能值。
        self.file_notary_type = file_notary_type
        # 哈希算法，当 file_notary_type 为 FILE_HASH 时，此返回值才有效。
        self.hash_algorithm = hash_algorithm
        # 文件下载地址，当 file_notary_type 为 FILE_RAW 时才有此值。
        self.oss_path = oss_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.file_hash is not None:
            result['file_hash'] = self.file_hash
        if self.file_notary_type is not None:
            result['file_notary_type'] = self.file_notary_type
        if self.hash_algorithm is not None:
            result['hash_algorithm'] = self.hash_algorithm
        if self.oss_path is not None:
            result['oss_path'] = self.oss_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('file_hash') is not None:
            self.file_hash = m.get('file_hash')
        if m.get('file_notary_type') is not None:
            self.file_notary_type = m.get('file_notary_type')
        if m.get('hash_algorithm') is not None:
            self.hash_algorithm = m.get('hash_algorithm')
        if m.get('oss_path') is not None:
            self.oss_path = m.get('oss_path')
        return self


class CreateSourceRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        location: Location = None,
        phase: str = None,
        properties: str = None,
        source_desc: str = None,
        source_file: str = None,
        source_name: str = None,
        transaction_id: str = None,
        tsr: bool = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 存证地点(如手机硬件ID，Wi-Fi地址，GPS位置，IP地址)
        self.location = location
        # 描述本条存证在存证事务中的阶段，用户可自行维护
        self.phase = phase
        # 扩展属性
        self.properties = properties
        # 原文文件描述
        self.source_desc = source_desc
        # 存证文件内容，对文件内容做base64编码后得到。例如文件内容为“test”，那么base64编码后的结果则为“dGVzdA==”
        self.source_file = source_file
        # 存证原文名称
        self.source_name = source_name
        # 存证事务ID
        self.transaction_id = transaction_id
        # 是否使用可信时间戳，默认为false
        self.tsr = tsr

    def validate(self):
        if self.location:
            self.location.validate()
        self.validate_required(self.phase, 'phase')
        self.validate_required(self.source_desc, 'source_desc')
        self.validate_required(self.source_file, 'source_file')
        self.validate_required(self.source_name, 'source_name')
        self.validate_required(self.transaction_id, 'transaction_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.properties is not None:
            result['properties'] = self.properties
        if self.source_desc is not None:
            result['source_desc'] = self.source_desc
        if self.source_file is not None:
            result['source_file'] = self.source_file
        if self.source_name is not None:
            result['source_name'] = self.source_name
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.tsr is not None:
            result['tsr'] = self.tsr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('location') is not None:
            temp_model = Location()
            self.location = temp_model.from_map(m['location'])
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('source_desc') is not None:
            self.source_desc = m.get('source_desc')
        if m.get('source_file') is not None:
            self.source_file = m.get('source_file')
        if m.get('source_name') is not None:
            self.source_name = m.get('source_name')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('tsr') is not None:
            self.tsr = m.get('tsr')
        return self


class CreateSourceResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        tsr: TsrResponse = None,
        tx_hash: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 可信时间信息
        self.tsr = tsr
        # 存证凭据
        self.tx_hash = tx_hash

    def validate(self):
        if self.tsr:
            self.tsr.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.tsr is not None:
            result['tsr'] = self.tsr.to_map()
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('tsr') is not None:
            temp_model = TsrResponse()
            self.tsr = temp_model.from_map(m['tsr'])
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class GetSourceRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        location: Location = None,
        phase: str = None,
        properties: str = None,
        transaction_id: str = None,
        tx_hash: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 存证地点(如手机硬件ID，Wi-Fi地址，GPS位置，IP地址)
        self.location = location
        # 描述本条存证在存证事务中的阶段，用户可自行维护
        self.phase = phase
        # 扩展属性
        self.properties = properties
        # 存证事务id
        self.transaction_id = transaction_id
        # 存证凭据
        self.tx_hash = tx_hash

    def validate(self):
        if self.location:
            self.location.validate()
        self.validate_required(self.tx_hash, 'tx_hash')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.properties is not None:
            result['properties'] = self.properties
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('location') is not None:
            temp_model = Location()
            self.location = temp_model.from_map(m['location'])
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class GetSourceResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        oss_path: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 文件下载地址
        self.oss_path = oss_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.oss_path is not None:
            result['oss_path'] = self.oss_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('oss_path') is not None:
            self.oss_path = m.get('oss_path')
        return self


class CheckStatusRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        notary_check_meta_list: List[NotaryCheckMeta] = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 存证核验数据组
        self.notary_check_meta_list = notary_check_meta_list

    def validate(self):
        self.validate_required(self.notary_check_meta_list, 'notary_check_meta_list')
        if self.notary_check_meta_list:
            for k in self.notary_check_meta_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        result['notary_check_meta_list'] = []
        if self.notary_check_meta_list is not None:
            for k in self.notary_check_meta_list:
                result['notary_check_meta_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        self.notary_check_meta_list = []
        if m.get('notary_check_meta_list') is not None:
            for k in m.get('notary_check_meta_list'):
                temp_model = NotaryCheckMeta()
                self.notary_check_meta_list.append(temp_model.from_map(k))
        return self


class CheckStatusResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        notary_check_results: List[NotaryCheckResult] = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 存证核验结果
        self.notary_check_results = notary_check_results

    def validate(self):
        if self.notary_check_results:
            for k in self.notary_check_results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        result['notary_check_results'] = []
        if self.notary_check_results is not None:
            for k in self.notary_check_results:
                result['notary_check_results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        self.notary_check_results = []
        if m.get('notary_check_results') is not None:
            for k in m.get('notary_check_results'):
                temp_model = NotaryCheckResult()
                self.notary_check_results.append(temp_model.from_map(k))
        return self


class DeployLeaseContractRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        contract_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 租赁服务平台对应的合约ID
        self.contract_id = contract_id

    def validate(self):
        self.validate_required(self.contract_id, 'contract_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.contract_id is not None:
            result['contract_id'] = self.contract_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('contract_id') is not None:
            self.contract_id = m.get('contract_id')
        return self


class DeployLeaseContractResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 状态码
        # 0表示成功
        self.code = code
        # 错误信息
        self.err_message = err_message
        # 合约部署成功的交易哈希
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class CreateLeaseProductinfoRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        application_id: str = None,
        deposit_price: int = None,
        install_price: int = None,
        lease_id: str = None,
        main_class: str = None,
        product_id: str = None,
        product_name: str = None,
        product_price: int = None,
        rentinfos: List[RentInfo] = None,
        sub_class: str = None,
        supplier_id: str = None,
        supplier_name: str = None,
        supplier_version: str = None,
        extra_info: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 合约id
        self.application_id = application_id
        # 保证金  精确到毫厘，即123400表示12.34元
        self.deposit_price = deposit_price
        # 安装拆卸费 精确到毫厘，即123400表示12.34元
        self.install_price = install_price
        # 租赁服务平台id
        self.lease_id = lease_id
        # 一级分类
        self.main_class = main_class
        # 商品编码 长度不可超过50
        self.product_id = product_id
        # 商品名称
        self.product_name = product_name
        # 采购价  精确到毫厘，即123400表示12.34元
        self.product_price = product_price
        # 出租详细信息
        self.rentinfos = rentinfos
        # 二级分类
        self.sub_class = sub_class
        # 供应商id
        self.supplier_id = supplier_id
        # 供应商
        self.supplier_name = supplier_name
        # 供应商对该产品版本
        self.supplier_version = supplier_version
        # 商品目录额外信息
        self.extra_info = extra_info

    def validate(self):
        self.validate_required(self.deposit_price, 'deposit_price')
        self.validate_required(self.install_price, 'install_price')
        self.validate_required(self.lease_id, 'lease_id')
        self.validate_required(self.main_class, 'main_class')
        self.validate_required(self.product_id, 'product_id')
        self.validate_required(self.product_name, 'product_name')
        self.validate_required(self.product_price, 'product_price')
        self.validate_required(self.rentinfos, 'rentinfos')
        if self.rentinfos:
            for k in self.rentinfos:
                if k:
                    k.validate()
        self.validate_required(self.sub_class, 'sub_class')
        self.validate_required(self.supplier_name, 'supplier_name')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.application_id is not None:
            result['application_id'] = self.application_id
        if self.deposit_price is not None:
            result['deposit_price'] = self.deposit_price
        if self.install_price is not None:
            result['install_price'] = self.install_price
        if self.lease_id is not None:
            result['lease_id'] = self.lease_id
        if self.main_class is not None:
            result['main_class'] = self.main_class
        if self.product_id is not None:
            result['product_id'] = self.product_id
        if self.product_name is not None:
            result['product_name'] = self.product_name
        if self.product_price is not None:
            result['product_price'] = self.product_price
        result['rentinfos'] = []
        if self.rentinfos is not None:
            for k in self.rentinfos:
                result['rentinfos'].append(k.to_map() if k else None)
        if self.sub_class is not None:
            result['sub_class'] = self.sub_class
        if self.supplier_id is not None:
            result['supplier_id'] = self.supplier_id
        if self.supplier_name is not None:
            result['supplier_name'] = self.supplier_name
        if self.supplier_version is not None:
            result['supplier_version'] = self.supplier_version
        if self.extra_info is not None:
            result['extra_info'] = self.extra_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('application_id') is not None:
            self.application_id = m.get('application_id')
        if m.get('deposit_price') is not None:
            self.deposit_price = m.get('deposit_price')
        if m.get('install_price') is not None:
            self.install_price = m.get('install_price')
        if m.get('lease_id') is not None:
            self.lease_id = m.get('lease_id')
        if m.get('main_class') is not None:
            self.main_class = m.get('main_class')
        if m.get('product_id') is not None:
            self.product_id = m.get('product_id')
        if m.get('product_name') is not None:
            self.product_name = m.get('product_name')
        if m.get('product_price') is not None:
            self.product_price = m.get('product_price')
        self.rentinfos = []
        if m.get('rentinfos') is not None:
            for k in m.get('rentinfos'):
                temp_model = RentInfo()
                self.rentinfos.append(temp_model.from_map(k))
        if m.get('sub_class') is not None:
            self.sub_class = m.get('sub_class')
        if m.get('supplier_id') is not None:
            self.supplier_id = m.get('supplier_id')
        if m.get('supplier_name') is not None:
            self.supplier_name = m.get('supplier_name')
        if m.get('supplier_version') is not None:
            self.supplier_version = m.get('supplier_version')
        if m.get('extra_info') is not None:
            self.extra_info = m.get('extra_info')
        return self


class CreateLeaseProductinfoResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 状态码 0表示成功
        self.code = code
        # 错误信息
        self.err_message = err_message
        # 用户信息存储到合约中对应的区块链交易哈希
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class AuthLeaseContractRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        credit_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 融资服务平台ID 长度不可超过50
        self.credit_id = credit_id

    def validate(self):
        self.validate_required(self.credit_id, 'credit_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.credit_id is not None:
            result['credit_id'] = self.credit_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('credit_id') is not None:
            self.credit_id = m.get('credit_id')
        return self


class AuthLeaseContractResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 状态码
        # 0表示成功
        self.code = code
        # 错误信息
        self.err_message = err_message
        # 授权信息存储到合约中对应的区块链交易哈希
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class CreateLeaseUserinfoRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        alipay_uid: str = None,
        application_id: str = None,
        async_: int = None,
        extra_info: str = None,
        lease_corp_id: str = None,
        lease_corp_name: str = None,
        lease_corp_owner_name: str = None,
        login_id: str = None,
        login_time: str = None,
        login_type: int = None,
        order_id: str = None,
        user_blockchain_verify_hash: str = None,
        user_email: str = None,
        user_id: str = None,
        user_image_hash: str = None,
        user_image_tx_hash: str = None,
        user_name: str = None,
        user_phone_number: str = None,
        user_type: int = None,
        related_notify: List[str] = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 支付宝账号信息
        self.alipay_uid = alipay_uid
        # 融资租赁业务id，由资方控制台生成返回
        self.application_id = application_id
        # 是否启动异步
        self.async_ = async_
        # 融资租赁用户信息额外字段
        self.extra_info = extra_info
        # 承租企业统一社会信用代码 长度不可超过50
        self.lease_corp_id = lease_corp_id
        # 承租企业名称 长度不可超过50
        self.lease_corp_name = lease_corp_name
        # 承租法定代表人姓名 长度不可超过50
        self.lease_corp_owner_name = lease_corp_owner_name
        # 用户登录名，租赁平台会员ID/支付宝ID 长度不可超过50
        self.login_id = login_id
        # 用户登录时间 格式为2019-8-31 12:00:00
        self.login_time = login_time
        # 用户登录名类型 1.商户会员2.支付宝3.其他
        self.login_type = login_type
        # 订单id 长度不可超过50
        self.order_id = order_id
        # 区块链认证Hash，若为支付宝实人，必填
        self.user_blockchain_verify_hash = user_blockchain_verify_hash
        # 承租人电子邮件，法院/仲裁电子送达必填项，长度不超过5
        self.user_email = user_email
        # 承租人身份证
        self.user_id = user_id
        # 承租人身份证照片哈希
        self.user_image_hash = user_image_hash
        # 承租人身份证照片存证交易哈希
        self.user_image_tx_hash = user_image_tx_hash
        # 承租人姓名 长度不可超过10
        self.user_name = user_name
        # 承租人手机号
        self.user_phone_number = user_phone_number
        # 身份认证类型 1支付宝实人，2芝麻实人，3非蚂蚁实人
        self.user_type = user_type
        # 额外通知第三方，如果需要通知相关方外的第三方，需要在此设置关联方的租户id，若不设置则只通知资方
        self.related_notify = related_notify

    def validate(self):
        self.validate_required(self.alipay_uid, 'alipay_uid')
        self.validate_required(self.lease_corp_id, 'lease_corp_id')
        self.validate_required(self.lease_corp_name, 'lease_corp_name')
        self.validate_required(self.lease_corp_owner_name, 'lease_corp_owner_name')
        self.validate_required(self.login_id, 'login_id')
        self.validate_required(self.login_time, 'login_time')
        self.validate_required(self.login_type, 'login_type')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.user_image_hash, 'user_image_hash')
        self.validate_required(self.user_image_tx_hash, 'user_image_tx_hash')
        self.validate_required(self.user_name, 'user_name')
        self.validate_required(self.user_phone_number, 'user_phone_number')
        self.validate_required(self.user_type, 'user_type')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.alipay_uid is not None:
            result['alipay_uid'] = self.alipay_uid
        if self.application_id is not None:
            result['application_id'] = self.application_id
        if self.async_ is not None:
            result['async'] = self.async_
        if self.extra_info is not None:
            result['extra_info'] = self.extra_info
        if self.lease_corp_id is not None:
            result['lease_corp_id'] = self.lease_corp_id
        if self.lease_corp_name is not None:
            result['lease_corp_name'] = self.lease_corp_name
        if self.lease_corp_owner_name is not None:
            result['lease_corp_owner_name'] = self.lease_corp_owner_name
        if self.login_id is not None:
            result['login_id'] = self.login_id
        if self.login_time is not None:
            result['login_time'] = self.login_time
        if self.login_type is not None:
            result['login_type'] = self.login_type
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.user_blockchain_verify_hash is not None:
            result['user_blockchain_verify_hash'] = self.user_blockchain_verify_hash
        if self.user_email is not None:
            result['user_email'] = self.user_email
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_image_hash is not None:
            result['user_image_hash'] = self.user_image_hash
        if self.user_image_tx_hash is not None:
            result['user_image_tx_hash'] = self.user_image_tx_hash
        if self.user_name is not None:
            result['user_name'] = self.user_name
        if self.user_phone_number is not None:
            result['user_phone_number'] = self.user_phone_number
        if self.user_type is not None:
            result['user_type'] = self.user_type
        if self.related_notify is not None:
            result['related_notify'] = self.related_notify
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('alipay_uid') is not None:
            self.alipay_uid = m.get('alipay_uid')
        if m.get('application_id') is not None:
            self.application_id = m.get('application_id')
        if m.get('async') is not None:
            self.async_ = m.get('async')
        if m.get('extra_info') is not None:
            self.extra_info = m.get('extra_info')
        if m.get('lease_corp_id') is not None:
            self.lease_corp_id = m.get('lease_corp_id')
        if m.get('lease_corp_name') is not None:
            self.lease_corp_name = m.get('lease_corp_name')
        if m.get('lease_corp_owner_name') is not None:
            self.lease_corp_owner_name = m.get('lease_corp_owner_name')
        if m.get('login_id') is not None:
            self.login_id = m.get('login_id')
        if m.get('login_time') is not None:
            self.login_time = m.get('login_time')
        if m.get('login_type') is not None:
            self.login_type = m.get('login_type')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('user_blockchain_verify_hash') is not None:
            self.user_blockchain_verify_hash = m.get('user_blockchain_verify_hash')
        if m.get('user_email') is not None:
            self.user_email = m.get('user_email')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_image_hash') is not None:
            self.user_image_hash = m.get('user_image_hash')
        if m.get('user_image_tx_hash') is not None:
            self.user_image_tx_hash = m.get('user_image_tx_hash')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        if m.get('user_phone_number') is not None:
            self.user_phone_number = m.get('user_phone_number')
        if m.get('user_type') is not None:
            self.user_type = m.get('user_type')
        if m.get('related_notify') is not None:
            self.related_notify = m.get('related_notify')
        return self


class CreateLeaseUserinfoResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 状态码 0表示成功
        self.code = code
        # 错误信息
        self.err_message = err_message
        # 用户信息存储到合约中对应的区块链交易哈希
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class CreateLeaseOrderinfoRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        acutal_pre_auth_free: int = None,
        application_id: str = None,
        async_: int = None,
        bill_url: str = None,
        buy_out_price: int = None,
        city_code: str = None,
        deposit_free: int = None,
        district_code: str = None,
        extra_info: str = None,
        install_hash: str = None,
        install_price: int = None,
        install_tx_hash: str = None,
        insurance_number: str = None,
        insurance_url: str = None,
        in_store_time: str = None,
        lease_order_extra: List[LeaseOrderExtra] = None,
        lease_service_additional_file_hash: str = None,
        lease_service_additional_file_tx_hash: str = None,
        lease_service_file_hash: str = None,
        lease_service_file_tx_hash: str = None,
        order_create_time: str = None,
        order_id: str = None,
        order_pay_id: str = None,
        order_pay_time: str = None,
        order_pay_type: int = None,
        out_store_deliver_number: str = None,
        out_store_time: str = None,
        pay_proof_url: str = None,
        pre_auth_pay_order_id: str = None,
        product_info: List[ProductInfo] = None,
        province_code: str = None,
        purchase_contract_bill_hash: str = None,
        purchase_contract_bill_tx_hash: str = None,
        purchase_contract_hash: str = None,
        purchase_contract_tx_hash: str = None,
        purchase_contract_url: str = None,
        related_notify: List[str] = None,
        rent_contract_url: str = None,
        rent_price_per_month: int = None,
        rent_term: int = None,
        sign_hash: str = None,
        sign_time: str = None,
        sign_tx_hash: str = None,
        store_type: int = None,
        supplement_protocol_url: str = None,
        supplier_isv_account: str = None,
        user_address: str = None,
        lease_service_contract_id: str = None,
        agreement_no: str = None,
        agreement_order_id: str = None,
        down_payment: int = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 实际预授权金额，芝麻信用免押金额 精确到毫厘，即123400表示12.34元
        self.acutal_pre_auth_free = acutal_pre_auth_free
        # 融资租赁业务id，由资方控制台创建返回
        self.application_id = application_id
        # 是否启动异步处理订单
        self.async_ = async_
        # 采购发票地址
        self.bill_url = bill_url
        # 到期买断价 精确到毫厘，即123400表示12.34元
        self.buy_out_price = buy_out_price
        # 市编码
        self.city_code = city_code
        # 免押金额 精确到毫厘，即123400表示12.34元
        self.deposit_free = deposit_free
        # 区编码
        self.district_code = district_code
        # 融资租赁额外字段
        self.extra_info = extra_info
        # 安装服务记录哈希
        self.install_hash = install_hash
        # 安装拆卸费 精确到毫厘，即123400表示12.34元
        self.install_price = install_price
        # 安装服务记录链上存证交易哈希
        self.install_tx_hash = install_tx_hash
        # 保险单号
        self.insurance_number = insurance_number
        # 保险链接
        self.insurance_url = insurance_url
        # 租赁物入库日  格式为2019-8-31 12:00:00
        self.in_store_time = in_store_time
        # 订单额外信息
        self.lease_order_extra = lease_order_extra
        # 融资租赁及服务协议之补充协议文件
        self.lease_service_additional_file_hash = lease_service_additional_file_hash
        # 融资租赁及服务协议之补充协议文件链上存证交易哈希
        self.lease_service_additional_file_tx_hash = lease_service_additional_file_tx_hash
        # 融资租赁及服务协议文件hash，三方协议
        self.lease_service_file_hash = lease_service_file_hash
        # 融资租赁及服务协议文件链上存证交易哈希
        self.lease_service_file_tx_hash = lease_service_file_tx_hash
        # 订单创建时间 格式为2019-8-31 12:00:00
        self.order_create_time = order_create_time
        # 订单id 长度不可超过50
        self.order_id = order_id
        # 支付订单ID
        self.order_pay_id = order_pay_id
        # 订单支付时间 格式为2019-8-31 12:00:00
        self.order_pay_time = order_pay_time
        # 订单支付类型 1 预授权，2信用套餐，3支付宝代扣，4其他
        self.order_pay_type = order_pay_type
        # 租赁物出库物流编号
        self.out_store_deliver_number = out_store_deliver_number
        # 租赁物出库日  格式为2019-8-31 12:00:00
        self.out_store_time = out_store_time
        # 支付凭证地址
        self.pay_proof_url = pay_proof_url
        # 预授权支付订单ID
        self.pre_auth_pay_order_id = pre_auth_pay_order_id
        # 产品详细信息
        self.product_info = product_info
        # 省编码
        self.province_code = province_code
        # 采购发票文件哈希
        self.purchase_contract_bill_hash = purchase_contract_bill_hash
        # 采购发票文件链上存证交易哈希
        self.purchase_contract_bill_tx_hash = purchase_contract_bill_tx_hash
        # 采购合同文件哈希
        self.purchase_contract_hash = purchase_contract_hash
        # 采购合同文件链上存证交易哈希
        self.purchase_contract_tx_hash = purchase_contract_tx_hash
        # 采购合同地址
        self.purchase_contract_url = purchase_contract_url
        # 额外通知第三方，如果需要通知相关方外的第三方，需要在此设置关联方的租户id，若不设置则只通知资方
        # 
        self.related_notify = related_notify
        # 租赁合同地址
        self.rent_contract_url = rent_contract_url
        # 月租金 精确到毫厘，即123400表示12.34元
        self.rent_price_per_month = rent_price_per_month
        # 租期
        self.rent_term = rent_term
        # 承租人签收记录哈希
        self.sign_hash = sign_hash
        # 承租人签收时间  格式为2019-8-31 12:00:00
        self.sign_time = sign_time
        # 承租人签收记录链上存证哈希
        self.sign_tx_hash = sign_tx_hash
        # 仓库类型 1实体仓 2虚拟仓
        self.store_type = store_type
        # 补充协议地址
        self.supplement_protocol_url = supplement_protocol_url
        # 供应商对应的金融科技租户id，若有此字段，则会授权相应的供应商上传采购等相关信息
        self.supplier_isv_account = supplier_isv_account
        # 承租人收货地址
        self.user_address = user_address
        # 智能合同的合同id
        self.lease_service_contract_id = lease_service_contract_id
        # 网商直付通模式的代扣协议号
        self.agreement_no = agreement_no
        # 直付通代扣受理订单号
        self.agreement_order_id = agreement_order_id
        # 单位是毫厘，123400
        self.down_payment = down_payment

    def validate(self):
        self.validate_required(self.acutal_pre_auth_free, 'acutal_pre_auth_free')
        self.validate_required(self.buy_out_price, 'buy_out_price')
        self.validate_required(self.deposit_free, 'deposit_free')
        if self.lease_order_extra:
            for k in self.lease_order_extra:
                if k:
                    k.validate()
        self.validate_required(self.lease_service_file_hash, 'lease_service_file_hash')
        self.validate_required(self.lease_service_file_tx_hash, 'lease_service_file_tx_hash')
        self.validate_required(self.order_create_time, 'order_create_time')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.order_pay_time, 'order_pay_time')
        self.validate_required(self.product_info, 'product_info')
        if self.product_info:
            for k in self.product_info:
                if k:
                    k.validate()
        self.validate_required(self.rent_price_per_month, 'rent_price_per_month')
        self.validate_required(self.rent_term, 'rent_term')
        self.validate_required(self.user_address, 'user_address')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.acutal_pre_auth_free is not None:
            result['acutal_pre_auth_free'] = self.acutal_pre_auth_free
        if self.application_id is not None:
            result['application_id'] = self.application_id
        if self.async_ is not None:
            result['async'] = self.async_
        if self.bill_url is not None:
            result['bill_url'] = self.bill_url
        if self.buy_out_price is not None:
            result['buy_out_price'] = self.buy_out_price
        if self.city_code is not None:
            result['city_code'] = self.city_code
        if self.deposit_free is not None:
            result['deposit_free'] = self.deposit_free
        if self.district_code is not None:
            result['district_code'] = self.district_code
        if self.extra_info is not None:
            result['extra_info'] = self.extra_info
        if self.install_hash is not None:
            result['install_hash'] = self.install_hash
        if self.install_price is not None:
            result['install_price'] = self.install_price
        if self.install_tx_hash is not None:
            result['install_tx_hash'] = self.install_tx_hash
        if self.insurance_number is not None:
            result['insurance_number'] = self.insurance_number
        if self.insurance_url is not None:
            result['insurance_url'] = self.insurance_url
        if self.in_store_time is not None:
            result['in_store_time'] = self.in_store_time
        result['lease_order_extra'] = []
        if self.lease_order_extra is not None:
            for k in self.lease_order_extra:
                result['lease_order_extra'].append(k.to_map() if k else None)
        if self.lease_service_additional_file_hash is not None:
            result['lease_service_additional_file_hash'] = self.lease_service_additional_file_hash
        if self.lease_service_additional_file_tx_hash is not None:
            result['lease_service_additional_file_tx_hash'] = self.lease_service_additional_file_tx_hash
        if self.lease_service_file_hash is not None:
            result['lease_service_file_hash'] = self.lease_service_file_hash
        if self.lease_service_file_tx_hash is not None:
            result['lease_service_file_tx_hash'] = self.lease_service_file_tx_hash
        if self.order_create_time is not None:
            result['order_create_time'] = self.order_create_time
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.order_pay_id is not None:
            result['order_pay_id'] = self.order_pay_id
        if self.order_pay_time is not None:
            result['order_pay_time'] = self.order_pay_time
        if self.order_pay_type is not None:
            result['order_pay_type'] = self.order_pay_type
        if self.out_store_deliver_number is not None:
            result['out_store_deliver_number'] = self.out_store_deliver_number
        if self.out_store_time is not None:
            result['out_store_time'] = self.out_store_time
        if self.pay_proof_url is not None:
            result['pay_proof_url'] = self.pay_proof_url
        if self.pre_auth_pay_order_id is not None:
            result['pre_auth_pay_order_id'] = self.pre_auth_pay_order_id
        result['product_info'] = []
        if self.product_info is not None:
            for k in self.product_info:
                result['product_info'].append(k.to_map() if k else None)
        if self.province_code is not None:
            result['province_code'] = self.province_code
        if self.purchase_contract_bill_hash is not None:
            result['purchase_contract_bill_hash'] = self.purchase_contract_bill_hash
        if self.purchase_contract_bill_tx_hash is not None:
            result['purchase_contract_bill_tx_hash'] = self.purchase_contract_bill_tx_hash
        if self.purchase_contract_hash is not None:
            result['purchase_contract_hash'] = self.purchase_contract_hash
        if self.purchase_contract_tx_hash is not None:
            result['purchase_contract_tx_hash'] = self.purchase_contract_tx_hash
        if self.purchase_contract_url is not None:
            result['purchase_contract_url'] = self.purchase_contract_url
        if self.related_notify is not None:
            result['related_notify'] = self.related_notify
        if self.rent_contract_url is not None:
            result['rent_contract_url'] = self.rent_contract_url
        if self.rent_price_per_month is not None:
            result['rent_price_per_month'] = self.rent_price_per_month
        if self.rent_term is not None:
            result['rent_term'] = self.rent_term
        if self.sign_hash is not None:
            result['sign_hash'] = self.sign_hash
        if self.sign_time is not None:
            result['sign_time'] = self.sign_time
        if self.sign_tx_hash is not None:
            result['sign_tx_hash'] = self.sign_tx_hash
        if self.store_type is not None:
            result['store_type'] = self.store_type
        if self.supplement_protocol_url is not None:
            result['supplement_protocol_url'] = self.supplement_protocol_url
        if self.supplier_isv_account is not None:
            result['supplier_isv_account'] = self.supplier_isv_account
        if self.user_address is not None:
            result['user_address'] = self.user_address
        if self.lease_service_contract_id is not None:
            result['lease_service_contract_id'] = self.lease_service_contract_id
        if self.agreement_no is not None:
            result['agreement_no'] = self.agreement_no
        if self.agreement_order_id is not None:
            result['agreement_order_id'] = self.agreement_order_id
        if self.down_payment is not None:
            result['down_payment'] = self.down_payment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('acutal_pre_auth_free') is not None:
            self.acutal_pre_auth_free = m.get('acutal_pre_auth_free')
        if m.get('application_id') is not None:
            self.application_id = m.get('application_id')
        if m.get('async') is not None:
            self.async_ = m.get('async')
        if m.get('bill_url') is not None:
            self.bill_url = m.get('bill_url')
        if m.get('buy_out_price') is not None:
            self.buy_out_price = m.get('buy_out_price')
        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')
        if m.get('deposit_free') is not None:
            self.deposit_free = m.get('deposit_free')
        if m.get('district_code') is not None:
            self.district_code = m.get('district_code')
        if m.get('extra_info') is not None:
            self.extra_info = m.get('extra_info')
        if m.get('install_hash') is not None:
            self.install_hash = m.get('install_hash')
        if m.get('install_price') is not None:
            self.install_price = m.get('install_price')
        if m.get('install_tx_hash') is not None:
            self.install_tx_hash = m.get('install_tx_hash')
        if m.get('insurance_number') is not None:
            self.insurance_number = m.get('insurance_number')
        if m.get('insurance_url') is not None:
            self.insurance_url = m.get('insurance_url')
        if m.get('in_store_time') is not None:
            self.in_store_time = m.get('in_store_time')
        self.lease_order_extra = []
        if m.get('lease_order_extra') is not None:
            for k in m.get('lease_order_extra'):
                temp_model = LeaseOrderExtra()
                self.lease_order_extra.append(temp_model.from_map(k))
        if m.get('lease_service_additional_file_hash') is not None:
            self.lease_service_additional_file_hash = m.get('lease_service_additional_file_hash')
        if m.get('lease_service_additional_file_tx_hash') is not None:
            self.lease_service_additional_file_tx_hash = m.get('lease_service_additional_file_tx_hash')
        if m.get('lease_service_file_hash') is not None:
            self.lease_service_file_hash = m.get('lease_service_file_hash')
        if m.get('lease_service_file_tx_hash') is not None:
            self.lease_service_file_tx_hash = m.get('lease_service_file_tx_hash')
        if m.get('order_create_time') is not None:
            self.order_create_time = m.get('order_create_time')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('order_pay_id') is not None:
            self.order_pay_id = m.get('order_pay_id')
        if m.get('order_pay_time') is not None:
            self.order_pay_time = m.get('order_pay_time')
        if m.get('order_pay_type') is not None:
            self.order_pay_type = m.get('order_pay_type')
        if m.get('out_store_deliver_number') is not None:
            self.out_store_deliver_number = m.get('out_store_deliver_number')
        if m.get('out_store_time') is not None:
            self.out_store_time = m.get('out_store_time')
        if m.get('pay_proof_url') is not None:
            self.pay_proof_url = m.get('pay_proof_url')
        if m.get('pre_auth_pay_order_id') is not None:
            self.pre_auth_pay_order_id = m.get('pre_auth_pay_order_id')
        self.product_info = []
        if m.get('product_info') is not None:
            for k in m.get('product_info'):
                temp_model = ProductInfo()
                self.product_info.append(temp_model.from_map(k))
        if m.get('province_code') is not None:
            self.province_code = m.get('province_code')
        if m.get('purchase_contract_bill_hash') is not None:
            self.purchase_contract_bill_hash = m.get('purchase_contract_bill_hash')
        if m.get('purchase_contract_bill_tx_hash') is not None:
            self.purchase_contract_bill_tx_hash = m.get('purchase_contract_bill_tx_hash')
        if m.get('purchase_contract_hash') is not None:
            self.purchase_contract_hash = m.get('purchase_contract_hash')
        if m.get('purchase_contract_tx_hash') is not None:
            self.purchase_contract_tx_hash = m.get('purchase_contract_tx_hash')
        if m.get('purchase_contract_url') is not None:
            self.purchase_contract_url = m.get('purchase_contract_url')
        if m.get('related_notify') is not None:
            self.related_notify = m.get('related_notify')
        if m.get('rent_contract_url') is not None:
            self.rent_contract_url = m.get('rent_contract_url')
        if m.get('rent_price_per_month') is not None:
            self.rent_price_per_month = m.get('rent_price_per_month')
        if m.get('rent_term') is not None:
            self.rent_term = m.get('rent_term')
        if m.get('sign_hash') is not None:
            self.sign_hash = m.get('sign_hash')
        if m.get('sign_time') is not None:
            self.sign_time = m.get('sign_time')
        if m.get('sign_tx_hash') is not None:
            self.sign_tx_hash = m.get('sign_tx_hash')
        if m.get('store_type') is not None:
            self.store_type = m.get('store_type')
        if m.get('supplement_protocol_url') is not None:
            self.supplement_protocol_url = m.get('supplement_protocol_url')
        if m.get('supplier_isv_account') is not None:
            self.supplier_isv_account = m.get('supplier_isv_account')
        if m.get('user_address') is not None:
            self.user_address = m.get('user_address')
        if m.get('lease_service_contract_id') is not None:
            self.lease_service_contract_id = m.get('lease_service_contract_id')
        if m.get('agreement_no') is not None:
            self.agreement_no = m.get('agreement_no')
        if m.get('agreement_order_id') is not None:
            self.agreement_order_id = m.get('agreement_order_id')
        if m.get('down_payment') is not None:
            self.down_payment = m.get('down_payment')
        return self


class CreateLeaseOrderinfoResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 状态码
        # 0 表示成功
        self.code = code
        # 错误信息
        self.err_message = err_message
        # 订单产品/服务信息存储到合约中对应的区块链交易哈希
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class CreateLeasePromiseRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        application_id: str = None,
        audit_mode: int = None,
        clearing_org: str = None,
        credit_org: str = None,
        first_pay_date: str = None,
        lease_alipay_uid: str = None,
        limit: int = None,
        order_id: str = None,
        pay_date_list: List[str] = None,
        pay_extra_info_list: List[str] = None,
        pay_money: int = None,
        pay_money_list: List[int] = None,
        pay_period: int = None,
        async_: int = None,
        down_payment_serial_number: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 融资租赁业务id，由资方控制台生成返回
        self.application_id = application_id
        # 审核方式,0为系统自动审核，1为人工审核
        self.audit_mode = audit_mode
        # 清分机构金融科技租户ID
        self.clearing_org = clearing_org
        # 放款机构金融科技租户ID
        self.credit_org = credit_org
        # 第一次还款时的日期
        self.first_pay_date = first_pay_date
        # 融资机构的阿里uid
        self.lease_alipay_uid = lease_alipay_uid
        # 宽限期，精确到毫秒
        self.limit = limit
        # 订单id 长度不可超过50
        self.order_id = order_id
        # 应付租金，精确到毫厘，即123400表示12.34元
        self.pay_date_list = pay_date_list
        # 租赁方承诺额外字段
        self.pay_extra_info_list = pay_extra_info_list
        # 应付租金 精确到毫厘，即123400表示12.34元
        # 
        self.pay_money = pay_money
        # 应付租金 精确到毫厘，即123400表示12.34元
        self.pay_money_list = pay_money_list
        # 应付租金的期数
        self.pay_period = pay_period
        # 是否启动异步订单处理
        self.async_ = async_
        # 首付款代扣流水号，最大长度是128
        self.down_payment_serial_number = down_payment_serial_number

    def validate(self):
        self.validate_required(self.audit_mode, 'audit_mode')
        self.validate_required(self.clearing_org, 'clearing_org')
        self.validate_required(self.credit_org, 'credit_org')
        self.validate_required(self.lease_alipay_uid, 'lease_alipay_uid')
        self.validate_required(self.limit, 'limit')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.pay_date_list, 'pay_date_list')
        self.validate_required(self.pay_money_list, 'pay_money_list')
        self.validate_required(self.pay_period, 'pay_period')
        if self.down_payment_serial_number is not None:
            self.validate_max_length(self.down_payment_serial_number, 'down_payment_serial_number', 128)

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.application_id is not None:
            result['application_id'] = self.application_id
        if self.audit_mode is not None:
            result['audit_mode'] = self.audit_mode
        if self.clearing_org is not None:
            result['clearing_org'] = self.clearing_org
        if self.credit_org is not None:
            result['credit_org'] = self.credit_org
        if self.first_pay_date is not None:
            result['first_pay_date'] = self.first_pay_date
        if self.lease_alipay_uid is not None:
            result['lease_alipay_uid'] = self.lease_alipay_uid
        if self.limit is not None:
            result['limit'] = self.limit
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.pay_date_list is not None:
            result['pay_date_list'] = self.pay_date_list
        if self.pay_extra_info_list is not None:
            result['pay_extra_info_list'] = self.pay_extra_info_list
        if self.pay_money is not None:
            result['pay_money'] = self.pay_money
        if self.pay_money_list is not None:
            result['pay_money_list'] = self.pay_money_list
        if self.pay_period is not None:
            result['pay_period'] = self.pay_period
        if self.async_ is not None:
            result['async'] = self.async_
        if self.down_payment_serial_number is not None:
            result['down_payment_serial_number'] = self.down_payment_serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('application_id') is not None:
            self.application_id = m.get('application_id')
        if m.get('audit_mode') is not None:
            self.audit_mode = m.get('audit_mode')
        if m.get('clearing_org') is not None:
            self.clearing_org = m.get('clearing_org')
        if m.get('credit_org') is not None:
            self.credit_org = m.get('credit_org')
        if m.get('first_pay_date') is not None:
            self.first_pay_date = m.get('first_pay_date')
        if m.get('lease_alipay_uid') is not None:
            self.lease_alipay_uid = m.get('lease_alipay_uid')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('pay_date_list') is not None:
            self.pay_date_list = m.get('pay_date_list')
        if m.get('pay_extra_info_list') is not None:
            self.pay_extra_info_list = m.get('pay_extra_info_list')
        if m.get('pay_money') is not None:
            self.pay_money = m.get('pay_money')
        if m.get('pay_money_list') is not None:
            self.pay_money_list = m.get('pay_money_list')
        if m.get('pay_period') is not None:
            self.pay_period = m.get('pay_period')
        if m.get('async') is not None:
            self.async_ = m.get('async')
        if m.get('down_payment_serial_number') is not None:
            self.down_payment_serial_number = m.get('down_payment_serial_number')
        return self


class CreateLeasePromiseResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 状态码
        self.code = code
        # 错误信息
        self.err_message = err_message
        # 租方承诺信息存储到合约中对应的区块链交易哈希
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class CreateLeaseVerifyinfoRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        application_id: str = None,
        async_: int = None,
        card_number: str = None,
        credit_end_time: str = None,
        credit_limit: int = None,
        credit_start_time: str = None,
        extra_info: str = None,
        lease_corp_id: str = None,
        lease_corp_name: str = None,
        lease_corp_owner_name: str = None,
        lease_id: str = None,
        loan: str = None,
        order_id: str = None,
        pay_back_hash: str = None,
        pay_back_tx_hash: str = None,
        user_id: str = None,
        user_name: str = None,
        user_phone_number: str = None,
        verify_result: int = None,
        voucher: str = None,
        verify_refuse_desc: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 融资租赁业务id，由资方控制台生成返回
        self.application_id = application_id
        # 是否启动订单的异步处理
        self.async_ = async_
        # 放款账户
        self.card_number = card_number
        # 授信终止时间，格式为"2019-07-31 12:00:00"
        self.credit_end_time = credit_end_time
        # 授信额度，精确到毫厘，即123400表示12.34元
        self.credit_limit = credit_limit
        # 授信起始时间，格式为"2019-07-31 12:00:00"
        self.credit_start_time = credit_start_time
        # 融资租赁审贷信息额外字段
        self.extra_info = extra_info
        # 承租企业统一社会信用代码 长度不可超过50
        self.lease_corp_id = lease_corp_id
        # 承租企业名称 长度不可超过50
        self.lease_corp_name = lease_corp_name
        # 承租法定代表人姓名 长度不可超过50
        self.lease_corp_owner_name = lease_corp_owner_name
        # 租赁服务平台id
        self.lease_id = lease_id
        # 放款流水单号
        self.loan = loan
        # 订单id 长度不可超过50
        self.order_id = order_id
        # 还款计划文件哈希
        self.pay_back_hash = pay_back_hash
        # 还款计划文件存证交易哈希
        self.pay_back_tx_hash = pay_back_tx_hash
        # 承租人身份证
        self.user_id = user_id
        # 承租人姓名 长度不可超过10
        self.user_name = user_name
        # 承租人手机号
        self.user_phone_number = user_phone_number
        # 是否通过，0表示不通过，1表示通过
        self.verify_result = verify_result
        # 付款汇款凭证 民盛转账成功后上传
        self.voucher = voucher
        # 拒绝的理由
        self.verify_refuse_desc = verify_refuse_desc

    def validate(self):
        self.validate_required(self.lease_id, 'lease_id')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.verify_result, 'verify_result')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.application_id is not None:
            result['application_id'] = self.application_id
        if self.async_ is not None:
            result['async'] = self.async_
        if self.card_number is not None:
            result['card_number'] = self.card_number
        if self.credit_end_time is not None:
            result['credit_end_time'] = self.credit_end_time
        if self.credit_limit is not None:
            result['credit_limit'] = self.credit_limit
        if self.credit_start_time is not None:
            result['credit_start_time'] = self.credit_start_time
        if self.extra_info is not None:
            result['extra_info'] = self.extra_info
        if self.lease_corp_id is not None:
            result['lease_corp_id'] = self.lease_corp_id
        if self.lease_corp_name is not None:
            result['lease_corp_name'] = self.lease_corp_name
        if self.lease_corp_owner_name is not None:
            result['lease_corp_owner_name'] = self.lease_corp_owner_name
        if self.lease_id is not None:
            result['lease_id'] = self.lease_id
        if self.loan is not None:
            result['loan'] = self.loan
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.pay_back_hash is not None:
            result['pay_back_hash'] = self.pay_back_hash
        if self.pay_back_tx_hash is not None:
            result['pay_back_tx_hash'] = self.pay_back_tx_hash
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        if self.user_phone_number is not None:
            result['user_phone_number'] = self.user_phone_number
        if self.verify_result is not None:
            result['verify_result'] = self.verify_result
        if self.voucher is not None:
            result['voucher'] = self.voucher
        if self.verify_refuse_desc is not None:
            result['verify_refuse_desc'] = self.verify_refuse_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('application_id') is not None:
            self.application_id = m.get('application_id')
        if m.get('async') is not None:
            self.async_ = m.get('async')
        if m.get('card_number') is not None:
            self.card_number = m.get('card_number')
        if m.get('credit_end_time') is not None:
            self.credit_end_time = m.get('credit_end_time')
        if m.get('credit_limit') is not None:
            self.credit_limit = m.get('credit_limit')
        if m.get('credit_start_time') is not None:
            self.credit_start_time = m.get('credit_start_time')
        if m.get('extra_info') is not None:
            self.extra_info = m.get('extra_info')
        if m.get('lease_corp_id') is not None:
            self.lease_corp_id = m.get('lease_corp_id')
        if m.get('lease_corp_name') is not None:
            self.lease_corp_name = m.get('lease_corp_name')
        if m.get('lease_corp_owner_name') is not None:
            self.lease_corp_owner_name = m.get('lease_corp_owner_name')
        if m.get('lease_id') is not None:
            self.lease_id = m.get('lease_id')
        if m.get('loan') is not None:
            self.loan = m.get('loan')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('pay_back_hash') is not None:
            self.pay_back_hash = m.get('pay_back_hash')
        if m.get('pay_back_tx_hash') is not None:
            self.pay_back_tx_hash = m.get('pay_back_tx_hash')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        if m.get('user_phone_number') is not None:
            self.user_phone_number = m.get('user_phone_number')
        if m.get('verify_result') is not None:
            self.verify_result = m.get('verify_result')
        if m.get('voucher') is not None:
            self.voucher = m.get('voucher')
        if m.get('verify_refuse_desc') is not None:
            self.verify_refuse_desc = m.get('verify_refuse_desc')
        return self


class CreateLeaseVerifyinfoResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 状态码
        # 0表示成功
        self.code = code
        # 错误信息
        self.err_message = err_message
        # 审贷信息存储到合约中对应的区块链交易哈希
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class CreateLeaseCreditpromiseRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        application_id: str = None,
        credit_promise_extra_info_list: List[str] = None,
        lease_id: str = None,
        order_id: str = None,
        pay_in_advance_money: int = None,
        pay_in_advance_money_list: List[int] = None,
        pay_in_advance_time: str = None,
        pay_in_advance_time_list: List[str] = None,
        promise_hash: str = None,
        promise_tx_hash: str = None,
        return_money: int = None,
        return_money_list: List[int] = None,
        return_rate: int = None,
        return_time: str = None,
        return_time_list: List[str] = None,
        async_: int = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 融资租赁业务id，由资方控制台创建返回
        self.application_id = application_id
        # 融资租赁承诺额外字段
        self.credit_promise_extra_info_list = credit_promise_extra_info_list
        # 租赁平台金融科技id
        self.lease_id = lease_id
        # 订单id 长度不可超过50
        self.order_id = order_id
        # 垫付金额
        self.pay_in_advance_money = pay_in_advance_money
        # 垫付金额，精确到毫厘，即123400表示12.34元
        self.pay_in_advance_money_list = pay_in_advance_money_list
        # 垫付日期
        self.pay_in_advance_time = pay_in_advance_time
        # 垫付日  格式为2019-8-31 12:00:00
        self.pay_in_advance_time_list = pay_in_advance_time_list
        # 根据融资租赁合同及其补充协议哈希
        self.promise_hash = promise_hash
        # 根据融资租赁合同及其补充协议存证交易hash
        self.promise_tx_hash = promise_tx_hash
        # 归还金额
        self.return_money = return_money
        # 还款金额，精确到毫厘，即123400表示12.34元
        self.return_money_list = return_money_list
        # 还款比例，精确到小数点后四位 12.34% 表示为1234
        self.return_rate = return_rate
        # 归还日，格式为"2019-07-31 12:00:00"
        self.return_time = return_time
        # 归还日，格式为"2019-07-31 12:00:00"
        self.return_time_list = return_time_list
        # 是否启动异步订单处理
        self.async_ = async_

    def validate(self):
        self.validate_required(self.lease_id, 'lease_id')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.pay_in_advance_time_list, 'pay_in_advance_time_list')
        self.validate_required(self.promise_hash, 'promise_hash')
        self.validate_required(self.promise_tx_hash, 'promise_tx_hash')
        self.validate_required(self.return_money_list, 'return_money_list')
        self.validate_required(self.return_time_list, 'return_time_list')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.application_id is not None:
            result['application_id'] = self.application_id
        if self.credit_promise_extra_info_list is not None:
            result['credit_promise_extra_info_list'] = self.credit_promise_extra_info_list
        if self.lease_id is not None:
            result['lease_id'] = self.lease_id
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.pay_in_advance_money is not None:
            result['pay_in_advance_money'] = self.pay_in_advance_money
        if self.pay_in_advance_money_list is not None:
            result['pay_in_advance_money_list'] = self.pay_in_advance_money_list
        if self.pay_in_advance_time is not None:
            result['pay_in_advance_time'] = self.pay_in_advance_time
        if self.pay_in_advance_time_list is not None:
            result['pay_in_advance_time_list'] = self.pay_in_advance_time_list
        if self.promise_hash is not None:
            result['promise_hash'] = self.promise_hash
        if self.promise_tx_hash is not None:
            result['promise_tx_hash'] = self.promise_tx_hash
        if self.return_money is not None:
            result['return_money'] = self.return_money
        if self.return_money_list is not None:
            result['return_money_list'] = self.return_money_list
        if self.return_rate is not None:
            result['return_rate'] = self.return_rate
        if self.return_time is not None:
            result['return_time'] = self.return_time
        if self.return_time_list is not None:
            result['return_time_list'] = self.return_time_list
        if self.async_ is not None:
            result['async'] = self.async_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('application_id') is not None:
            self.application_id = m.get('application_id')
        if m.get('credit_promise_extra_info_list') is not None:
            self.credit_promise_extra_info_list = m.get('credit_promise_extra_info_list')
        if m.get('lease_id') is not None:
            self.lease_id = m.get('lease_id')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('pay_in_advance_money') is not None:
            self.pay_in_advance_money = m.get('pay_in_advance_money')
        if m.get('pay_in_advance_money_list') is not None:
            self.pay_in_advance_money_list = m.get('pay_in_advance_money_list')
        if m.get('pay_in_advance_time') is not None:
            self.pay_in_advance_time = m.get('pay_in_advance_time')
        if m.get('pay_in_advance_time_list') is not None:
            self.pay_in_advance_time_list = m.get('pay_in_advance_time_list')
        if m.get('promise_hash') is not None:
            self.promise_hash = m.get('promise_hash')
        if m.get('promise_tx_hash') is not None:
            self.promise_tx_hash = m.get('promise_tx_hash')
        if m.get('return_money') is not None:
            self.return_money = m.get('return_money')
        if m.get('return_money_list') is not None:
            self.return_money_list = m.get('return_money_list')
        if m.get('return_rate') is not None:
            self.return_rate = m.get('return_rate')
        if m.get('return_time') is not None:
            self.return_time = m.get('return_time')
        if m.get('return_time_list') is not None:
            self.return_time_list = m.get('return_time_list')
        if m.get('async') is not None:
            self.async_ = m.get('async')
        return self


class CreateLeaseCreditpromiseResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 状态码
        # 0表示成功
        self.code = code
        # 错误信息
        self.err_message = err_message
        # 资方承诺信息存储到合约中对应的区块链交易哈希
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class CreateLeaseDisburseinfoRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        active_account: str = None,
        active_result_desc: str = None,
        active_result_status: int = None,
        active_return_date: str = None,
        active_return_money: int = None,
        disburse_limit: int = None,
        disburse_money: int = None,
        disburse_service: int = None,
        exceed_duration: int = None,
        exceed_pay_back_status: int = None,
        exceed_rate: int = None,
        exceed_return_money: int = None,
        loan_rate: int = None,
        order_id: str = None,
        pay_back_date: str = None,
        pay_back_money: int = None,
        return_interest: int = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 共管账户，网商清分
        self.active_account = active_account
        # 对结果的简要描述信息
        self.active_result_desc = active_result_desc
        # 成功/失败 0表示失败，1表示成功
        self.active_result_status = active_result_status
        # 授信成功日期，格式为"2019-07-31 12:00:00"
        self.active_return_date = active_return_date
        # 本金+利息，精确到毫厘，即123400表示12.34元
        self.active_return_money = active_return_money
        # 支用期限，精确到毫秒
        self.disburse_limit = disburse_limit
        # 支用金额，精确到毫厘，即123400表示12.34元
        self.disburse_money = disburse_money
        # 支用科目，服务费/租金，精确到毫厘，即123400表示12.34元
        self.disburse_service = disburse_service
        # 逾期天数，支用到期日开始计算，天数为单位
        self.exceed_duration = exceed_duration
        # 1未还款，2已还款
        self.exceed_pay_back_status = exceed_pay_back_status
        # 逾期利率，精确到小数点后四位 12.34% 表示为1234
        self.exceed_rate = exceed_rate
        # 逾期应还款总额，本金+利息+逾期利息，精确到毫厘，即123400表示12.34元
        self.exceed_return_money = exceed_return_money
        # 贷款利率,银行同步利率，年化8%-15%,精确到小数点后四位 12.34% 表示为1234
        self.loan_rate = loan_rate
        # 订单id 长度不可超过50
        self.order_id = order_id
        # 到期还款日，T+支用期限，节假日顺延至第一个工作日，格式为"2019-07-31 12:00:00"
        self.pay_back_date = pay_back_date
        # 到期还款金额，本金+利息，精确到毫厘，即123400表示12.34元
        self.pay_back_money = pay_back_money
        # 应还利息，系统自动计算当日应还利息（T+1），精确到毫厘，即123400表示12.34元
        self.return_interest = return_interest

    def validate(self):
        self.validate_required(self.active_account, 'active_account')
        self.validate_required(self.active_result_desc, 'active_result_desc')
        self.validate_required(self.active_result_status, 'active_result_status')
        self.validate_required(self.active_return_date, 'active_return_date')
        self.validate_required(self.active_return_money, 'active_return_money')
        self.validate_required(self.disburse_limit, 'disburse_limit')
        self.validate_required(self.disburse_money, 'disburse_money')
        self.validate_required(self.disburse_service, 'disburse_service')
        self.validate_required(self.exceed_duration, 'exceed_duration')
        self.validate_required(self.exceed_pay_back_status, 'exceed_pay_back_status')
        self.validate_required(self.exceed_rate, 'exceed_rate')
        self.validate_required(self.exceed_return_money, 'exceed_return_money')
        self.validate_required(self.loan_rate, 'loan_rate')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.pay_back_date, 'pay_back_date')
        self.validate_required(self.pay_back_money, 'pay_back_money')
        self.validate_required(self.return_interest, 'return_interest')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.active_account is not None:
            result['active_account'] = self.active_account
        if self.active_result_desc is not None:
            result['active_result_desc'] = self.active_result_desc
        if self.active_result_status is not None:
            result['active_result_status'] = self.active_result_status
        if self.active_return_date is not None:
            result['active_return_date'] = self.active_return_date
        if self.active_return_money is not None:
            result['active_return_money'] = self.active_return_money
        if self.disburse_limit is not None:
            result['disburse_limit'] = self.disburse_limit
        if self.disburse_money is not None:
            result['disburse_money'] = self.disburse_money
        if self.disburse_service is not None:
            result['disburse_service'] = self.disburse_service
        if self.exceed_duration is not None:
            result['exceed_duration'] = self.exceed_duration
        if self.exceed_pay_back_status is not None:
            result['exceed_pay_back_status'] = self.exceed_pay_back_status
        if self.exceed_rate is not None:
            result['exceed_rate'] = self.exceed_rate
        if self.exceed_return_money is not None:
            result['exceed_return_money'] = self.exceed_return_money
        if self.loan_rate is not None:
            result['loan_rate'] = self.loan_rate
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.pay_back_date is not None:
            result['pay_back_date'] = self.pay_back_date
        if self.pay_back_money is not None:
            result['pay_back_money'] = self.pay_back_money
        if self.return_interest is not None:
            result['return_interest'] = self.return_interest
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('active_account') is not None:
            self.active_account = m.get('active_account')
        if m.get('active_result_desc') is not None:
            self.active_result_desc = m.get('active_result_desc')
        if m.get('active_result_status') is not None:
            self.active_result_status = m.get('active_result_status')
        if m.get('active_return_date') is not None:
            self.active_return_date = m.get('active_return_date')
        if m.get('active_return_money') is not None:
            self.active_return_money = m.get('active_return_money')
        if m.get('disburse_limit') is not None:
            self.disburse_limit = m.get('disburse_limit')
        if m.get('disburse_money') is not None:
            self.disburse_money = m.get('disburse_money')
        if m.get('disburse_service') is not None:
            self.disburse_service = m.get('disburse_service')
        if m.get('exceed_duration') is not None:
            self.exceed_duration = m.get('exceed_duration')
        if m.get('exceed_pay_back_status') is not None:
            self.exceed_pay_back_status = m.get('exceed_pay_back_status')
        if m.get('exceed_rate') is not None:
            self.exceed_rate = m.get('exceed_rate')
        if m.get('exceed_return_money') is not None:
            self.exceed_return_money = m.get('exceed_return_money')
        if m.get('loan_rate') is not None:
            self.loan_rate = m.get('loan_rate')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('pay_back_date') is not None:
            self.pay_back_date = m.get('pay_back_date')
        if m.get('pay_back_money') is not None:
            self.pay_back_money = m.get('pay_back_money')
        if m.get('return_interest') is not None:
            self.return_interest = m.get('return_interest')
        return self


class CreateLeaseDisburseinfoResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 状态码
        # 0表示成功
        self.code = code
        # 错误信息描述
        self.err_message = err_message
        # 贷后字段存储到合约中对应的区块链交易哈希
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class QueryLeaseOrderinfoRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        application_id: str = None,
        lease_id: str = None,
        order_id: str = None,
        phase_info: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 融资租赁业务id，由资方控制台生成返回
        self.application_id = application_id
        # 租赁平台金融科技租户id
        self.lease_id = lease_id
        # 订单id 长度不可超过50
        self.order_id = order_id
        # 阶段描述
        self.phase_info = phase_info

    def validate(self):
        self.validate_required(self.lease_id, 'lease_id')
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.application_id is not None:
            result['application_id'] = self.application_id
        if self.lease_id is not None:
            result['lease_id'] = self.lease_id
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.phase_info is not None:
            result['phase_info'] = self.phase_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('application_id') is not None:
            self.application_id = m.get('application_id')
        if m.get('lease_id') is not None:
            self.lease_id = m.get('lease_id')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('phase_info') is not None:
            self.phase_info = m.get('phase_info')
        return self


class QueryLeaseOrderinfoResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 错误码
        # 0表示成功
        self.code = code
        # 错误信息描述
        self.err_message = err_message
        # 订单详细信息
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class CreateFinanceTextnotaryRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        cert_no: str = None,
        hash_algorithm: str = None,
        location: Location = None,
        mobile: str = None,
        phase: str = None,
        properties: str = None,
        text_hash: str = None,
        transaction_id: str = None,
        tsr: bool = None,
        user_name: str = None,
        third_message_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 反欺诈查询对应的身份证号码
        self.cert_no = cert_no
        # 哈希算法
        self.hash_algorithm = hash_algorithm
        # 位置描述信息
        self.location = location
        # 反欺诈查询需要的手机号码
        self.mobile = mobile
        # 存证阶段，用户可自行维护
        self.phase = phase
        # 扩展属性
        self.properties = properties
        # 文本哈希
        self.text_hash = text_hash
        # 存证事务ID
        self.transaction_id = transaction_id
        # 是否使用可信时间戳
        self.tsr = tsr
        # 反欺诈查询需要的姓名
        self.user_name = user_name
        # 本次请求的唯一id
        self.third_message_id = third_message_id

    def validate(self):
        self.validate_required(self.hash_algorithm, 'hash_algorithm')
        if self.location:
            self.location.validate()
        self.validate_required(self.phase, 'phase')
        self.validate_required(self.text_hash, 'text_hash')
        self.validate_required(self.transaction_id, 'transaction_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.cert_no is not None:
            result['cert_no'] = self.cert_no
        if self.hash_algorithm is not None:
            result['hash_algorithm'] = self.hash_algorithm
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.phase is not None:
            result['phase'] = self.phase
        if self.properties is not None:
            result['properties'] = self.properties
        if self.text_hash is not None:
            result['text_hash'] = self.text_hash
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.tsr is not None:
            result['tsr'] = self.tsr
        if self.user_name is not None:
            result['user_name'] = self.user_name
        if self.third_message_id is not None:
            result['third_message_id'] = self.third_message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('cert_no') is not None:
            self.cert_no = m.get('cert_no')
        if m.get('hash_algorithm') is not None:
            self.hash_algorithm = m.get('hash_algorithm')
        if m.get('location') is not None:
            temp_model = Location()
            self.location = temp_model.from_map(m['location'])
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('text_hash') is not None:
            self.text_hash = m.get('text_hash')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('tsr') is not None:
            self.tsr = m.get('tsr')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        if m.get('third_message_id') is not None:
            self.third_message_id = m.get('third_message_id')
        return self


class CreateFinanceTextnotaryResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        credit_risk_score: str = None,
        tsr: TsrResponse = None,
        tx_hash: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 反欺诈对应的信用值
        self.credit_risk_score = credit_risk_score
        # 可信时间戳
        self.tsr = tsr
        # 交易哈希
        self.tx_hash = tx_hash

    def validate(self):
        if self.tsr:
            self.tsr.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.credit_risk_score is not None:
            result['credit_risk_score'] = self.credit_risk_score
        if self.tsr is not None:
            result['tsr'] = self.tsr.to_map()
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('credit_risk_score') is not None:
            self.credit_risk_score = m.get('credit_risk_score')
        if m.get('tsr') is not None:
            temp_model = TsrResponse()
            self.tsr = temp_model.from_map(m['tsr'])
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class GetFinanceTextnotaryRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        location: Location = None,
        phase: str = None,
        properties: str = None,
        transaction_id: str = None,
        tx_hash: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 位置信息
        self.location = location
        # 存证阶段
        self.phase = phase
        # 扩展属性，用户可自行维护
        self.properties = properties
        # 存证事务ID
        self.transaction_id = transaction_id
        # 交易哈希
        self.tx_hash = tx_hash

    def validate(self):
        if self.location:
            self.location.validate()
        self.validate_required(self.tx_hash, 'tx_hash')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.properties is not None:
            result['properties'] = self.properties
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('location') is not None:
            temp_model = Location()
            self.location = temp_model.from_map(m['location'])
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class GetFinanceTextnotaryResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        hash_algorithm: str = None,
        text_hash: str = None,
        tsr: TsrResponse = None,
        phase: str = None,
        properties: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 哈希算法
        self.hash_algorithm = hash_algorithm
        # 文本哈希
        self.text_hash = text_hash
        # 可信时间戳
        self.tsr = tsr
        # 存证阶段
        self.phase = phase
        # 扩展属性
        self.properties = properties

    def validate(self):
        if self.tsr:
            self.tsr.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.hash_algorithm is not None:
            result['hash_algorithm'] = self.hash_algorithm
        if self.text_hash is not None:
            result['text_hash'] = self.text_hash
        if self.tsr is not None:
            result['tsr'] = self.tsr.to_map()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.properties is not None:
            result['properties'] = self.properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('hash_algorithm') is not None:
            self.hash_algorithm = m.get('hash_algorithm')
        if m.get('text_hash') is not None:
            self.text_hash = m.get('text_hash')
        if m.get('tsr') is not None:
            temp_model = TsrResponse()
            self.tsr = temp_model.from_map(m['tsr'])
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        return self


class CreateFinanceFilenotaryRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        cert_no: str = None,
        created_date: int = None,
        file_name: str = None,
        file_notary_type: str = None,
        file_size: int = None,
        file_type: str = None,
        file_url: str = None,
        hash_algorithm: str = None,
        location: Location = None,
        mobile: str = None,
        notary_content: str = None,
        phase: str = None,
        properties: str = None,
        transaction_id: str = None,
        tsr: bool = None,
        user_name: str = None,
        third_message_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 反欺诈需要的证件号码
        self.cert_no = cert_no
        # 创建日期，时间戳类型，单位毫秒
        self.created_date = created_date
        # 存证文件名称
        self.file_name = file_name
        # 文件存证类型，支持小于 1M 源文件或者文件哈希
        self.file_notary_type = file_notary_type
        # 文件大小，单位 Bytes
        self.file_size = file_size
        # 文件类型
        self.file_type = file_type
        # 文件地址
        self.file_url = file_url
        # 哈希算法
        self.hash_algorithm = hash_algorithm
        # 位置信息
        self.location = location
        # 反欺诈查询需要的手机号
        self.mobile = mobile
        # 文件存证内容
        self.notary_content = notary_content
        # 存证阶段
        self.phase = phase
        # 扩展属性，用户可自行维护
        self.properties = properties
        # 存证事务ID
        self.transaction_id = transaction_id
        # 是否使用可信时间戳
        self.tsr = tsr
        # 反欺诈查询需要的证件上的姓名
        self.user_name = user_name
        # 本次请求的唯一ID
        self.third_message_id = third_message_id

    def validate(self):
        self.validate_required(self.created_date, 'created_date')
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.file_notary_type, 'file_notary_type')
        self.validate_required(self.file_type, 'file_type')
        if self.location:
            self.location.validate()
        self.validate_required(self.notary_content, 'notary_content')
        self.validate_required(self.phase, 'phase')
        self.validate_required(self.transaction_id, 'transaction_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.cert_no is not None:
            result['cert_no'] = self.cert_no
        if self.created_date is not None:
            result['created_date'] = self.created_date
        if self.file_name is not None:
            result['file_name'] = self.file_name
        if self.file_notary_type is not None:
            result['file_notary_type'] = self.file_notary_type
        if self.file_size is not None:
            result['file_size'] = self.file_size
        if self.file_type is not None:
            result['file_type'] = self.file_type
        if self.file_url is not None:
            result['file_url'] = self.file_url
        if self.hash_algorithm is not None:
            result['hash_algorithm'] = self.hash_algorithm
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.notary_content is not None:
            result['notary_content'] = self.notary_content
        if self.phase is not None:
            result['phase'] = self.phase
        if self.properties is not None:
            result['properties'] = self.properties
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.tsr is not None:
            result['tsr'] = self.tsr
        if self.user_name is not None:
            result['user_name'] = self.user_name
        if self.third_message_id is not None:
            result['third_message_id'] = self.third_message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('cert_no') is not None:
            self.cert_no = m.get('cert_no')
        if m.get('created_date') is not None:
            self.created_date = m.get('created_date')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        if m.get('file_notary_type') is not None:
            self.file_notary_type = m.get('file_notary_type')
        if m.get('file_size') is not None:
            self.file_size = m.get('file_size')
        if m.get('file_type') is not None:
            self.file_type = m.get('file_type')
        if m.get('file_url') is not None:
            self.file_url = m.get('file_url')
        if m.get('hash_algorithm') is not None:
            self.hash_algorithm = m.get('hash_algorithm')
        if m.get('location') is not None:
            temp_model = Location()
            self.location = temp_model.from_map(m['location'])
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('notary_content') is not None:
            self.notary_content = m.get('notary_content')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('tsr') is not None:
            self.tsr = m.get('tsr')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        if m.get('third_message_id') is not None:
            self.third_message_id = m.get('third_message_id')
        return self


class CreateFinanceFilenotaryResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        credit_risk_score: str = None,
        tsr: TsrResponse = None,
        tx_hash: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 反欺诈查询返回的信用值
        self.credit_risk_score = credit_risk_score
        # 可信时间戳
        self.tsr = tsr
        # 交易哈希
        self.tx_hash = tx_hash

    def validate(self):
        if self.tsr:
            self.tsr.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.credit_risk_score is not None:
            result['credit_risk_score'] = self.credit_risk_score
        if self.tsr is not None:
            result['tsr'] = self.tsr.to_map()
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('credit_risk_score') is not None:
            self.credit_risk_score = m.get('credit_risk_score')
        if m.get('tsr') is not None:
            temp_model = TsrResponse()
            self.tsr = temp_model.from_map(m['tsr'])
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class GetFinanceFilenotaryRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        location: Location = None,
        phase: str = None,
        properties: str = None,
        transaction_id: str = None,
        tx_hash: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 位置信息
        self.location = location
        # 存证状态
        self.phase = phase
        # 扩展属性，用户自行维护
        self.properties = properties
        # 存证事务ID
        self.transaction_id = transaction_id
        # 交易哈希
        self.tx_hash = tx_hash

    def validate(self):
        if self.location:
            self.location.validate()
        self.validate_required(self.tx_hash, 'tx_hash')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.properties is not None:
            result['properties'] = self.properties
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('location') is not None:
            temp_model = Location()
            self.location = temp_model.from_map(m['location'])
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class GetFinanceFilenotaryResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        file_name: str = None,
        file_notary_type: str = None,
        hash_algorithm: str = None,
        notary_content: str = None,
        phase: str = None,
        properties: str = None,
        tsr: TsrResponse = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 存证文件名称
        self.file_name = file_name
        # 文件存证类型
        self.file_notary_type = file_notary_type
        # 哈希算法
        self.hash_algorithm = hash_algorithm
        # FILE_HASH 模式时该值为文件哈希；FILE_RAW 模式时该值为临时 oss 下载地址
        self.notary_content = notary_content
        # 存证阶段
        self.phase = phase
        # 扩展属性
        self.properties = properties
        # 可信时间戳
        self.tsr = tsr

    def validate(self):
        if self.tsr:
            self.tsr.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.file_name is not None:
            result['file_name'] = self.file_name
        if self.file_notary_type is not None:
            result['file_notary_type'] = self.file_notary_type
        if self.hash_algorithm is not None:
            result['hash_algorithm'] = self.hash_algorithm
        if self.notary_content is not None:
            result['notary_content'] = self.notary_content
        if self.phase is not None:
            result['phase'] = self.phase
        if self.properties is not None:
            result['properties'] = self.properties
        if self.tsr is not None:
            result['tsr'] = self.tsr.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        if m.get('file_notary_type') is not None:
            self.file_notary_type = m.get('file_notary_type')
        if m.get('hash_algorithm') is not None:
            self.hash_algorithm = m.get('hash_algorithm')
        if m.get('notary_content') is not None:
            self.notary_content = m.get('notary_content')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('tsr') is not None:
            temp_model = TsrResponse()
            self.tsr = temp_model.from_map(m['tsr'])
        return self


class CheckIndustryNotaryRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        industry_type: str = None,
        notary_check_meta_list: List[NotaryCheckMeta] = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 行业类型
        self.industry_type = industry_type
        # 核验数据列表
        self.notary_check_meta_list = notary_check_meta_list

    def validate(self):
        self.validate_required(self.industry_type, 'industry_type')
        self.validate_required(self.notary_check_meta_list, 'notary_check_meta_list')
        if self.notary_check_meta_list:
            for k in self.notary_check_meta_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.industry_type is not None:
            result['industry_type'] = self.industry_type
        result['notary_check_meta_list'] = []
        if self.notary_check_meta_list is not None:
            for k in self.notary_check_meta_list:
                result['notary_check_meta_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('industry_type') is not None:
            self.industry_type = m.get('industry_type')
        self.notary_check_meta_list = []
        if m.get('notary_check_meta_list') is not None:
            for k in m.get('notary_check_meta_list'):
                temp_model = NotaryCheckMeta()
                self.notary_check_meta_list.append(temp_model.from_map(k))
        return self


class CheckIndustryNotaryResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        notary_check_results: List[NotaryCheckResult] = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 核验结果数组
        self.notary_check_results = notary_check_results

    def validate(self):
        if self.notary_check_results:
            for k in self.notary_check_results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        result['notary_check_results'] = []
        if self.notary_check_results is not None:
            for k in self.notary_check_results:
                result['notary_check_results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        self.notary_check_results = []
        if m.get('notary_check_results') is not None:
            for k in m.get('notary_check_results'):
                temp_model = NotaryCheckResult()
                self.notary_check_results.append(temp_model.from_map(k))
        return self


class UpdateLeaseContractRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        contract_id: str = None,
        application_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 被升级的合约名称
        self.contract_id = contract_id
        # 合约业务层id
        self.application_id = application_id

    def validate(self):
        self.validate_required(self.contract_id, 'contract_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.contract_id is not None:
            result['contract_id'] = self.contract_id
        if self.application_id is not None:
            result['application_id'] = self.application_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('contract_id') is not None:
            self.contract_id = m.get('contract_id')
        if m.get('application_id') is not None:
            self.application_id = m.get('application_id')
        return self


class UpdateLeaseContractResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 状态码 0表示成功
        self.code = code
        # 错误信息
        # 
        self.err_message = err_message
        # 升级合约所在的区块链交易哈希
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class CreateSueBreakpromiseinfoRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        order_id: str = None,
        user_id: str = None,
        user_name: str = None,
        phone_number: str = None,
        email: str = None,
        pre_sue_id: str = None,
        promise_date: str = None,
        promise_limit: int = None,
        sue_date: str = None,
        initiator_id: str = None,
        initiator_name: str = None,
        court_name: str = None,
        court_id: str = None,
        break_promise_money: int = None,
        business_class: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 合同唯一标识
        # 
        self.order_id = order_id
        # 当事人身份证号
        self.user_id = user_id
        # 当事人姓名
        self.user_name = user_name
        # 当事人手机号
        self.phone_number = phone_number
        # 当事人邮箱地址
        self.email = email
        # 诉前Id
        self.pre_sue_id = pre_sue_id
        # 应履约日期，格式为"2019-07-31 12:00:00"
        self.promise_date = promise_date
        # 宽限期(天数，从应履约日期到进行诉前违约惩戒的自然日数）
        self.promise_limit = promise_limit
        # 起诉期，格式为"2019-07-31 12:00:00"
        # 
        self.sue_date = sue_date
        # 商户统一社会信用代码或个人身份证
        self.initiator_id = initiator_id
        # 商户或个人名称
        # 
        self.initiator_name = initiator_name
        # 管辖法院名称
        self.court_name = court_name
        # 法院唯一标识
        self.court_id = court_id
        # 违约金额，精确到毫厘，即123400表示12.34元
        self.break_promise_money = break_promise_money
        # 所属行业
        self.business_class = business_class

    def validate(self):
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.user_name, 'user_name')
        self.validate_required(self.phone_number, 'phone_number')
        self.validate_required(self.email, 'email')
        self.validate_required(self.pre_sue_id, 'pre_sue_id')
        self.validate_required(self.promise_date, 'promise_date')
        self.validate_required(self.promise_limit, 'promise_limit')
        self.validate_required(self.sue_date, 'sue_date')
        self.validate_required(self.initiator_id, 'initiator_id')
        self.validate_required(self.initiator_name, 'initiator_name')
        self.validate_required(self.court_name, 'court_name')
        self.validate_required(self.court_id, 'court_id')
        self.validate_required(self.break_promise_money, 'break_promise_money')
        self.validate_required(self.business_class, 'business_class')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        if self.phone_number is not None:
            result['phone_number'] = self.phone_number
        if self.email is not None:
            result['email'] = self.email
        if self.pre_sue_id is not None:
            result['pre_sue_id'] = self.pre_sue_id
        if self.promise_date is not None:
            result['promise_date'] = self.promise_date
        if self.promise_limit is not None:
            result['promise_limit'] = self.promise_limit
        if self.sue_date is not None:
            result['sue_date'] = self.sue_date
        if self.initiator_id is not None:
            result['initiator_id'] = self.initiator_id
        if self.initiator_name is not None:
            result['initiator_name'] = self.initiator_name
        if self.court_name is not None:
            result['court_name'] = self.court_name
        if self.court_id is not None:
            result['court_id'] = self.court_id
        if self.break_promise_money is not None:
            result['break_promise_money'] = self.break_promise_money
        if self.business_class is not None:
            result['business_class'] = self.business_class
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        if m.get('phone_number') is not None:
            self.phone_number = m.get('phone_number')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('pre_sue_id') is not None:
            self.pre_sue_id = m.get('pre_sue_id')
        if m.get('promise_date') is not None:
            self.promise_date = m.get('promise_date')
        if m.get('promise_limit') is not None:
            self.promise_limit = m.get('promise_limit')
        if m.get('sue_date') is not None:
            self.sue_date = m.get('sue_date')
        if m.get('initiator_id') is not None:
            self.initiator_id = m.get('initiator_id')
        if m.get('initiator_name') is not None:
            self.initiator_name = m.get('initiator_name')
        if m.get('court_name') is not None:
            self.court_name = m.get('court_name')
        if m.get('court_id') is not None:
            self.court_id = m.get('court_id')
        if m.get('break_promise_money') is not None:
            self.break_promise_money = m.get('break_promise_money')
        if m.get('business_class') is not None:
            self.business_class = m.get('business_class')
        return self


class CreateSueBreakpromiseinfoResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        response_data: str = None,
        code: str = None,
        err_message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 成功插入违约数据到区块链的交易哈希
        self.response_data = response_data
        # 状态码,0表示成功
        # 
        self.code = code
        # 错误信息
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.response_data is not None:
            result['response_data'] = self.response_data
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        return self


class UpdateSueBreakpromiseinfoRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        order_id: str = None,
        phone_number: str = None,
        email: str = None,
        pre_sue_id: str = None,
        promise_date: str = None,
        promise_limit: int = None,
        sue_date: str = None,
        break_promise_money: int = None,
        business_class: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 合同唯一标识，不可更新
        # 
        self.order_id = order_id
        # 当事人手机号
        self.phone_number = phone_number
        # 当事人电子邮箱地址
        self.email = email
        # 诉前Id，不可更新
        # 
        self.pre_sue_id = pre_sue_id
        # 应履约日期，格式为"2019-07-31 12:00:00"
        self.promise_date = promise_date
        # 宽限期(天数，从应履约日期到进行诉前违约惩戒的自然日数）
        self.promise_limit = promise_limit
        # 起诉期，格式为"2019-07-31 12:00:00"
        self.sue_date = sue_date
        # 违约金额，精确到毫厘，即123400表示12.34元
        self.break_promise_money = break_promise_money
        # 所属行业
        # 
        self.business_class = business_class

    def validate(self):
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.phone_number, 'phone_number')
        self.validate_required(self.email, 'email')
        self.validate_required(self.pre_sue_id, 'pre_sue_id')
        self.validate_required(self.promise_date, 'promise_date')
        self.validate_required(self.promise_limit, 'promise_limit')
        self.validate_required(self.sue_date, 'sue_date')
        self.validate_required(self.break_promise_money, 'break_promise_money')
        self.validate_required(self.business_class, 'business_class')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.phone_number is not None:
            result['phone_number'] = self.phone_number
        if self.email is not None:
            result['email'] = self.email
        if self.pre_sue_id is not None:
            result['pre_sue_id'] = self.pre_sue_id
        if self.promise_date is not None:
            result['promise_date'] = self.promise_date
        if self.promise_limit is not None:
            result['promise_limit'] = self.promise_limit
        if self.sue_date is not None:
            result['sue_date'] = self.sue_date
        if self.break_promise_money is not None:
            result['break_promise_money'] = self.break_promise_money
        if self.business_class is not None:
            result['business_class'] = self.business_class
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('phone_number') is not None:
            self.phone_number = m.get('phone_number')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('pre_sue_id') is not None:
            self.pre_sue_id = m.get('pre_sue_id')
        if m.get('promise_date') is not None:
            self.promise_date = m.get('promise_date')
        if m.get('promise_limit') is not None:
            self.promise_limit = m.get('promise_limit')
        if m.get('sue_date') is not None:
            self.sue_date = m.get('sue_date')
        if m.get('break_promise_money') is not None:
            self.break_promise_money = m.get('break_promise_money')
        if m.get('business_class') is not None:
            self.business_class = m.get('business_class')
        return self


class UpdateSueBreakpromiseinfoResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        response_data: str = None,
        code: int = None,
        err_message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 违约案件信息提交对应的区块链交易哈希
        self.response_data = response_data
        # 状态码,0表示成功
        # 
        self.code = code
        # 错误信息
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.response_data is not None:
            result['response_data'] = self.response_data
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        return self


class DeleteSueBreakpromiseinfoRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        order_id: str = None,
        pre_sue_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 合同唯一标识，不可更新
        self.order_id = order_id
        # 诉前id，不可更新
        self.pre_sue_id = pre_sue_id

    def validate(self):
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.pre_sue_id, 'pre_sue_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.pre_sue_id is not None:
            result['pre_sue_id'] = self.pre_sue_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('pre_sue_id') is not None:
            self.pre_sue_id = m.get('pre_sue_id')
        return self


class DeleteSueBreakpromiseinfoResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        response_data: str = None,
        code: int = None,
        err_message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 违约案件信息提交对应的区块链交易哈希
        self.response_data = response_data
        # 状态码 0表示成功
        self.code = code
        # 错误信息
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.response_data is not None:
            result['response_data'] = self.response_data
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        return self


class QuerySueUserinfoRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        user_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 被查者身份证号
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class QuerySueUserinfoResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: int = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 状态码 0表示成功
        self.code = code
        # 错误信息
        self.err_message = err_message
        # 用户违约个数
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class UpdateSueExeplarycontractRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        contract_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 合约名称
        self.contract_id = contract_id

    def validate(self):
        self.validate_required(self.contract_id, 'contract_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.contract_id is not None:
            result['contract_id'] = self.contract_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('contract_id') is not None:
            self.contract_id = m.get('contract_id')
        return self


class UpdateSueExeplarycontractResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        response_data: str = None,
        code: int = None,
        err_message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 0xabcdef123324234
        self.response_data = response_data
        # 状态码 0表示成功
        self.code = code
        # 错误信息
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.response_data is not None:
            result['response_data'] = self.response_data
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        return self


class UpdateSueExemplaryrevertRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        contract_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 用户管理合约id
        self.contract_id = contract_id

    def validate(self):
        self.validate_required(self.contract_id, 'contract_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.contract_id is not None:
            result['contract_id'] = self.contract_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('contract_id') is not None:
            self.contract_id = m.get('contract_id')
        return self


class UpdateSueExemplaryrevertResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        response_data: str = None,
        code: int = None,
        err_message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 回退合约所对应的区块链交易哈希
        self.response_data = response_data
        # 错误码 0表示成功
        self.code = code
        # 错误信息描述
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.response_data is not None:
            result['response_data'] = self.response_data
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        return self


class CreateLeaseAuditRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        application_id: str = None,
        async_: int = None,
        batch_index: str = None,
        current_audit_index: int = None,
        extra_info: str = None,
        lease_id: str = None,
        manual_audit: int = None,
        manual_audit_comments: str = None,
        order_id: str = None,
        total_audit_number: int = None,
        related_notify: List[str] = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 融资租赁业务id，由资方控制台创建返回
        self.application_id = application_id
        # 是否启动订单的异步处理
        self.async_ = async_
        # 融资机构审核批次
        # 
        self.batch_index = batch_index
        # 当前订单处于本批次中的index
        self.current_audit_index = current_audit_index
        # 融资租赁额外字段
        self.extra_info = extra_info
        # 租赁服务平台ID 长度不可超过50
        self.lease_id = lease_id
        # 融资机构审核状态，0.审核中1.审核失败2.审核成功
        self.manual_audit = manual_audit
        # 融资结构审核说明，非必填，审核失败必填失败原因
        self.manual_audit_comments = manual_audit_comments
        # 订单id 长度不可超过50
        # 
        self.order_id = order_id
        # 总审核的个数
        self.total_audit_number = total_audit_number
        # 额外通知第三方，如果需要通知相关方外的第三方，需要在此设置关联方的租户id，若不设置则只通知资方
        # 
        self.related_notify = related_notify

    def validate(self):
        self.validate_required(self.lease_id, 'lease_id')
        self.validate_required(self.manual_audit, 'manual_audit')
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.application_id is not None:
            result['application_id'] = self.application_id
        if self.async_ is not None:
            result['async'] = self.async_
        if self.batch_index is not None:
            result['batch_index'] = self.batch_index
        if self.current_audit_index is not None:
            result['current_audit_index'] = self.current_audit_index
        if self.extra_info is not None:
            result['extra_info'] = self.extra_info
        if self.lease_id is not None:
            result['lease_id'] = self.lease_id
        if self.manual_audit is not None:
            result['manual_audit'] = self.manual_audit
        if self.manual_audit_comments is not None:
            result['manual_audit_comments'] = self.manual_audit_comments
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.total_audit_number is not None:
            result['total_audit_number'] = self.total_audit_number
        if self.related_notify is not None:
            result['related_notify'] = self.related_notify
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('application_id') is not None:
            self.application_id = m.get('application_id')
        if m.get('async') is not None:
            self.async_ = m.get('async')
        if m.get('batch_index') is not None:
            self.batch_index = m.get('batch_index')
        if m.get('current_audit_index') is not None:
            self.current_audit_index = m.get('current_audit_index')
        if m.get('extra_info') is not None:
            self.extra_info = m.get('extra_info')
        if m.get('lease_id') is not None:
            self.lease_id = m.get('lease_id')
        if m.get('manual_audit') is not None:
            self.manual_audit = m.get('manual_audit')
        if m.get('manual_audit_comments') is not None:
            self.manual_audit_comments = m.get('manual_audit_comments')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('total_audit_number') is not None:
            self.total_audit_number = m.get('total_audit_number')
        if m.get('related_notify') is not None:
            self.related_notify = m.get('related_notify')
        return self


class CreateLeaseAuditResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 0表示成功
        self.code = code
        # 错误信息
        # 
        self.err_message = err_message
        # 融资平台审核订单信息存储到合约中对应的区块链交易哈希
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class CreateLeasePaymentfileRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        application_id: str = None,
        async_: int = None,
        extra_info: str = None,
        lease_id: str = None,
        order_id: str = None,
        payment_file_hash: str = None,
        payment_file_tx_hash: str = None,
        payment_url: str = None,
        related_notify: List[str] = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 融资租赁业务id，由资方控制台生成
        self.application_id = application_id
        # 是否启动订单的异步处理
        self.async_ = async_
        # 融资租赁额外字段
        self.extra_info = extra_info
        # 租赁服务平台ID 长度不可超过50
        self.lease_id = lease_id
        # 订单id 长度不可超过50
        self.order_id = order_id
        # 付款通知书加签完电子签名后，PDF文件hash
        self.payment_file_hash = payment_file_hash
        # 付款通知书存证交易哈希
        self.payment_file_tx_hash = payment_file_tx_hash
        # 付款通知所在路径
        self.payment_url = payment_url
        # 额外通知第三方，如果需要通知相关方外的第三方，需要在此设置关联方的租户id，若不设置则只通知资方
        # 
        self.related_notify = related_notify

    def validate(self):
        self.validate_required(self.lease_id, 'lease_id')
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.application_id is not None:
            result['application_id'] = self.application_id
        if self.async_ is not None:
            result['async'] = self.async_
        if self.extra_info is not None:
            result['extra_info'] = self.extra_info
        if self.lease_id is not None:
            result['lease_id'] = self.lease_id
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.payment_file_hash is not None:
            result['payment_file_hash'] = self.payment_file_hash
        if self.payment_file_tx_hash is not None:
            result['payment_file_tx_hash'] = self.payment_file_tx_hash
        if self.payment_url is not None:
            result['payment_url'] = self.payment_url
        if self.related_notify is not None:
            result['related_notify'] = self.related_notify
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('application_id') is not None:
            self.application_id = m.get('application_id')
        if m.get('async') is not None:
            self.async_ = m.get('async')
        if m.get('extra_info') is not None:
            self.extra_info = m.get('extra_info')
        if m.get('lease_id') is not None:
            self.lease_id = m.get('lease_id')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('payment_file_hash') is not None:
            self.payment_file_hash = m.get('payment_file_hash')
        if m.get('payment_file_tx_hash') is not None:
            self.payment_file_tx_hash = m.get('payment_file_tx_hash')
        if m.get('payment_url') is not None:
            self.payment_url = m.get('payment_url')
        if m.get('related_notify') is not None:
            self.related_notify = m.get('related_notify')
        return self


class CreateLeasePaymentfileResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 状态码 0表示成功
        # 
        self.code = code
        # 错误信息
        # 
        self.err_message = err_message
        # 租赁平台上传付款通知到合约中对应
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class CreateLeaseRentalRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        application_id: str = None,
        charge: int = None,
        extra_info: str = None,
        is_finish: bool = None,
        lease_term_index: int = None,
        order_id: str = None,
        remain_rental: int = None,
        remain_term: int = None,
        rental_money: int = None,
        rental_return_state: int = None,
        return_time: str = None,
        return_voucher_serial: str = None,
        return_voucher_type: int = None,
        return_way: int = None,
        async_: int = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 融资租赁业务id，由资方控制台生成返回
        self.application_id = application_id
        # 手续费，如通过预授权、代扣的方式规划，必填
        self.charge = charge
        # 融资租赁用户还款额外字段
        self.extra_info = extra_info
        # 是否本订单所有租金还款状态结束
        self.is_finish = is_finish
        # 租期编号，从1开始
        self.lease_term_index = lease_term_index
        # 订单id 长度不可超过50
        self.order_id = order_id
        # 剩余租金总数,会核验剩余租金与承诺等额
        self.remain_rental = remain_rental
        # 剩余归还期数
        self.remain_term = remain_term
        # 租金归还金额,精确到毫厘，即123400表示12.34元
        self.rental_money = rental_money
        # 租金归还状态，1.足额归还2.部分归还3.未归还
        self.rental_return_state = rental_return_state
        # 归还时间，格式为"2019-07-31 12:00:00"
        self.return_time = return_time
        # 还款凭证编号，不超过128字符，1.支付宝流水号
        self.return_voucher_serial = return_voucher_serial
        # 还款凭证类型，1.支付宝2.平台代收（客户主动还款）3.其他
        self.return_voucher_type = return_voucher_type
        # 归还方式，1.预授权代扣2.支付宝代扣3.主动还款4.其他
        self.return_way = return_way
        # 是否启动订单的异步处理
        self.async_ = async_

    def validate(self):
        self.validate_required(self.charge, 'charge')
        self.validate_required(self.is_finish, 'is_finish')
        self.validate_required(self.lease_term_index, 'lease_term_index')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.remain_rental, 'remain_rental')
        self.validate_required(self.remain_term, 'remain_term')
        self.validate_required(self.rental_money, 'rental_money')
        self.validate_required(self.rental_return_state, 'rental_return_state')
        self.validate_required(self.return_time, 'return_time')
        self.validate_required(self.return_voucher_serial, 'return_voucher_serial')
        self.validate_required(self.return_voucher_type, 'return_voucher_type')
        self.validate_required(self.return_way, 'return_way')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.application_id is not None:
            result['application_id'] = self.application_id
        if self.charge is not None:
            result['charge'] = self.charge
        if self.extra_info is not None:
            result['extra_info'] = self.extra_info
        if self.is_finish is not None:
            result['is_finish'] = self.is_finish
        if self.lease_term_index is not None:
            result['lease_term_index'] = self.lease_term_index
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.remain_rental is not None:
            result['remain_rental'] = self.remain_rental
        if self.remain_term is not None:
            result['remain_term'] = self.remain_term
        if self.rental_money is not None:
            result['rental_money'] = self.rental_money
        if self.rental_return_state is not None:
            result['rental_return_state'] = self.rental_return_state
        if self.return_time is not None:
            result['return_time'] = self.return_time
        if self.return_voucher_serial is not None:
            result['return_voucher_serial'] = self.return_voucher_serial
        if self.return_voucher_type is not None:
            result['return_voucher_type'] = self.return_voucher_type
        if self.return_way is not None:
            result['return_way'] = self.return_way
        if self.async_ is not None:
            result['async'] = self.async_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('application_id') is not None:
            self.application_id = m.get('application_id')
        if m.get('charge') is not None:
            self.charge = m.get('charge')
        if m.get('extra_info') is not None:
            self.extra_info = m.get('extra_info')
        if m.get('is_finish') is not None:
            self.is_finish = m.get('is_finish')
        if m.get('lease_term_index') is not None:
            self.lease_term_index = m.get('lease_term_index')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('remain_rental') is not None:
            self.remain_rental = m.get('remain_rental')
        if m.get('remain_term') is not None:
            self.remain_term = m.get('remain_term')
        if m.get('rental_money') is not None:
            self.rental_money = m.get('rental_money')
        if m.get('rental_return_state') is not None:
            self.rental_return_state = m.get('rental_return_state')
        if m.get('return_time') is not None:
            self.return_time = m.get('return_time')
        if m.get('return_voucher_serial') is not None:
            self.return_voucher_serial = m.get('return_voucher_serial')
        if m.get('return_voucher_type') is not None:
            self.return_voucher_type = m.get('return_voucher_type')
        if m.get('return_way') is not None:
            self.return_way = m.get('return_way')
        if m.get('async') is not None:
            self.async_ = m.get('async')
        return self


class CreateLeaseRentalResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 状态码 0表示成功
        self.code = code
        # 错误信息
        # 
        self.err_message = err_message
        # 租金归还记录上传到链上的哈希
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class CreateLeaseClearingRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        application_id: str = None,
        clearing_account: str = None,
        clearing_money: int = None,
        clearing_order_ids: List[str] = None,
        clearing_state: int = None,
        end_time: str = None,
        extra_info: str = None,
        lease_id: str = None,
        order_id: str = None,
        return_index: int = None,
        start_time: str = None,
        async_: int = None,
        memo: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 融资租赁业务id，由资方控制台创建返回
        self.application_id = application_id
        # 清分收款账号 长度不超过64
        self.clearing_account = clearing_account
        # 清分金额,精确到毫厘，即123400表示12.34元
        self.clearing_money = clearing_money
        # 清分订单号 长度不超过128
        self.clearing_order_ids = clearing_order_ids
        # 清分状态,1.足额2.部分3.零
        self.clearing_state = clearing_state
        # 结束时间，格式为"2019-07-31 12:00:00"
        self.end_time = end_time
        # 融资租赁额外字段
        self.extra_info = extra_info
        # 租赁平台商户Id 长度不可超过50
        self.lease_id = lease_id
        # 订单id 长度不可超过50
        # 
        self.order_id = order_id
        # 还款批次
        self.return_index = return_index
        # 开始时间，格式为"2019-07-31 12:00:00"
        self.start_time = start_time
        # 是否启动订单的异步处理
        self.async_ = async_
        # 清分资金的来源，比如用户xx元，商家yy元
        self.memo = memo

    def validate(self):
        self.validate_required(self.clearing_account, 'clearing_account')
        self.validate_required(self.clearing_money, 'clearing_money')
        self.validate_required(self.clearing_order_ids, 'clearing_order_ids')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.lease_id, 'lease_id')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.return_index, 'return_index')
        self.validate_required(self.start_time, 'start_time')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.application_id is not None:
            result['application_id'] = self.application_id
        if self.clearing_account is not None:
            result['clearing_account'] = self.clearing_account
        if self.clearing_money is not None:
            result['clearing_money'] = self.clearing_money
        if self.clearing_order_ids is not None:
            result['clearing_order_ids'] = self.clearing_order_ids
        if self.clearing_state is not None:
            result['clearing_state'] = self.clearing_state
        if self.end_time is not None:
            result['end_time'] = self.end_time
        if self.extra_info is not None:
            result['extra_info'] = self.extra_info
        if self.lease_id is not None:
            result['lease_id'] = self.lease_id
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.return_index is not None:
            result['return_index'] = self.return_index
        if self.start_time is not None:
            result['start_time'] = self.start_time
        if self.async_ is not None:
            result['async'] = self.async_
        if self.memo is not None:
            result['memo'] = self.memo
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('application_id') is not None:
            self.application_id = m.get('application_id')
        if m.get('clearing_account') is not None:
            self.clearing_account = m.get('clearing_account')
        if m.get('clearing_money') is not None:
            self.clearing_money = m.get('clearing_money')
        if m.get('clearing_order_ids') is not None:
            self.clearing_order_ids = m.get('clearing_order_ids')
        if m.get('clearing_state') is not None:
            self.clearing_state = m.get('clearing_state')
        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')
        if m.get('extra_info') is not None:
            self.extra_info = m.get('extra_info')
        if m.get('lease_id') is not None:
            self.lease_id = m.get('lease_id')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('return_index') is not None:
            self.return_index = m.get('return_index')
        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')
        if m.get('async') is not None:
            self.async_ = m.get('async')
        if m.get('memo') is not None:
            self.memo = m.get('memo')
        return self


class CreateLeaseClearingResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 状态码 0表示成功
        self.code = code
        # 错误信息
        # 
        self.err_message = err_message
        # 清分信息链上交易哈希
        # 
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class CreateLeaseRepaymentRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        application_id: str = None,
        extra_info: str = None,
        is_finish: bool = None,
        lease_id: str = None,
        order_id: str = None,
        overdue_day: int = None,
        overdue_money: int = None,
        overdue_rate: int = None,
        overdue_status: int = None,
        remain_return_money: int = None,
        remain_return_term: int = None,
        repayment_unique_id: str = None,
        return_description: str = None,
        return_index: int = None,
        return_money: int = None,
        return_status: int = None,
        return_time: str = None,
        source: int = None,
        status: int = None,
        async_: int = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 融资租赁业务id，由资方控制台生成返回
        self.application_id = application_id
        # 融资租赁租户还款额外字段
        self.extra_info = extra_info
        # 是否最终订单还款结束
        self.is_finish = is_finish
        # 租赁平台商户Id 长度不可超过50
        self.lease_id = lease_id
        # 订单id 长度不可超过50
        # 
        self.order_id = order_id
        # 逾期天数,支用到期日开始计算
        self.overdue_day = overdue_day
        # 逾期应还款总额,本金+利息+逾期利息,精确到毫厘，即123400表示12.34元
        self.overdue_money = overdue_money
        # 逾期利率（日利率）,精确到小数点后四位 12.34% 表示为1234
        self.overdue_rate = overdue_rate
        # 逾期状态,暂时都以0处理，目前不处理
        self.overdue_status = overdue_status
        # 剩余应还金额，精确到毫厘，即123400表示12.34元
        self.remain_return_money = remain_return_money
        # 剩余应还期数
        # 
        self.remain_return_term = remain_return_term
        # 每次还款流水凭证，需要融资方确认，id一样则不处理
        self.repayment_unique_id = repayment_unique_id
        # 还款结果简要描述,长度不超过256
        self.return_description = return_description
        # 还款批次
        # 
        self.return_index = return_index
        # 还款总额,本金+利息，精确到毫厘，即123400表示12.34元
        self.return_money = return_money
        # 还款结果状态,1.成功 2.失败
        self.return_status = return_status
        # 还款日期，格式为"2019-07-31 12:00:00"
        self.return_time = return_time
        # 还款来源,1.共管账号，2.网商清分
        self.source = source
        # 逾期后还款状态,1未还款,2已还款
        self.status = status
        # 是否启动订单的异步处理
        self.async_ = async_

    def validate(self):
        self.validate_required(self.is_finish, 'is_finish')
        self.validate_required(self.lease_id, 'lease_id')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.remain_return_money, 'remain_return_money')
        self.validate_required(self.remain_return_term, 'remain_return_term')
        self.validate_required(self.repayment_unique_id, 'repayment_unique_id')
        self.validate_required(self.return_description, 'return_description')
        self.validate_required(self.return_index, 'return_index')
        self.validate_required(self.return_money, 'return_money')
        self.validate_required(self.return_status, 'return_status')
        self.validate_required(self.return_time, 'return_time')
        self.validate_required(self.source, 'source')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.application_id is not None:
            result['application_id'] = self.application_id
        if self.extra_info is not None:
            result['extra_info'] = self.extra_info
        if self.is_finish is not None:
            result['is_finish'] = self.is_finish
        if self.lease_id is not None:
            result['lease_id'] = self.lease_id
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.overdue_day is not None:
            result['overdue_day'] = self.overdue_day
        if self.overdue_money is not None:
            result['overdue_money'] = self.overdue_money
        if self.overdue_rate is not None:
            result['overdue_rate'] = self.overdue_rate
        if self.overdue_status is not None:
            result['overdue_status'] = self.overdue_status
        if self.remain_return_money is not None:
            result['remain_return_money'] = self.remain_return_money
        if self.remain_return_term is not None:
            result['remain_return_term'] = self.remain_return_term
        if self.repayment_unique_id is not None:
            result['repayment_unique_id'] = self.repayment_unique_id
        if self.return_description is not None:
            result['return_description'] = self.return_description
        if self.return_index is not None:
            result['return_index'] = self.return_index
        if self.return_money is not None:
            result['return_money'] = self.return_money
        if self.return_status is not None:
            result['return_status'] = self.return_status
        if self.return_time is not None:
            result['return_time'] = self.return_time
        if self.source is not None:
            result['source'] = self.source
        if self.status is not None:
            result['status'] = self.status
        if self.async_ is not None:
            result['async'] = self.async_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('application_id') is not None:
            self.application_id = m.get('application_id')
        if m.get('extra_info') is not None:
            self.extra_info = m.get('extra_info')
        if m.get('is_finish') is not None:
            self.is_finish = m.get('is_finish')
        if m.get('lease_id') is not None:
            self.lease_id = m.get('lease_id')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('overdue_day') is not None:
            self.overdue_day = m.get('overdue_day')
        if m.get('overdue_money') is not None:
            self.overdue_money = m.get('overdue_money')
        if m.get('overdue_rate') is not None:
            self.overdue_rate = m.get('overdue_rate')
        if m.get('overdue_status') is not None:
            self.overdue_status = m.get('overdue_status')
        if m.get('remain_return_money') is not None:
            self.remain_return_money = m.get('remain_return_money')
        if m.get('remain_return_term') is not None:
            self.remain_return_term = m.get('remain_return_term')
        if m.get('repayment_unique_id') is not None:
            self.repayment_unique_id = m.get('repayment_unique_id')
        if m.get('return_description') is not None:
            self.return_description = m.get('return_description')
        if m.get('return_index') is not None:
            self.return_index = m.get('return_index')
        if m.get('return_money') is not None:
            self.return_money = m.get('return_money')
        if m.get('return_status') is not None:
            self.return_status = m.get('return_status')
        if m.get('return_time') is not None:
            self.return_time = m.get('return_time')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('async') is not None:
            self.async_ = m.get('async')
        return self


class CreateLeaseRepaymentResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 状态码 0表示成功
        self.code = code
        # 错误信息
        self.err_message = err_message
        # 融资租赁金融机构上传还款信息链上交易哈希值
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class CreateLeaseNotifyregisterRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        return self


class CreateLeaseNotifyregisterResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 0表示成功
        self.code = code
        # 错误描述
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        return self


class QueryLeaseIotinfoRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        end_time: str = None,
        product_imei_id: str = None,
        start_time: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 查询截止时间
        self.end_time = end_time
        # 设备唯一id imei id
        self.product_imei_id = product_imei_id
        # 查询开启时间
        self.start_time = start_time

    def validate(self):
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.product_imei_id, 'product_imei_id')
        self.validate_required(self.start_time, 'start_time')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.end_time is not None:
            result['end_time'] = self.end_time
        if self.product_imei_id is not None:
            result['product_imei_id'] = self.product_imei_id
        if self.start_time is not None:
            result['start_time'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')
        if m.get('product_imei_id') is not None:
            self.product_imei_id = m.get('product_imei_id')
        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')
        return self


class QueryLeaseIotinfoResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        lease_iot_item_info: List[LeaseIotItemInfo] = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 错误码
        self.code = code
        # ""
        self.err_message = err_message
        # 设备详情
        self.lease_iot_item_info = lease_iot_item_info

    def validate(self):
        if self.lease_iot_item_info:
            for k in self.lease_iot_item_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        result['lease_iot_item_info'] = []
        if self.lease_iot_item_info is not None:
            for k in self.lease_iot_item_info:
                result['lease_iot_item_info'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        self.lease_iot_item_info = []
        if m.get('lease_iot_item_info') is not None:
            for k in m.get('lease_iot_item_info'):
                temp_model = LeaseIotItemInfo()
                self.lease_iot_item_info.append(temp_model.from_map(k))
        return self


class CreateCourtTextnotaryRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        agency_code: str = None,
        application_code: str = None,
        business_type: str = None,
        data_type: str = None,
        location: Location = None,
        phase: str = None,
        properties: str = None,
        text_content: str = None,
        transaction_id: str = None,
        tsr: bool = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 对应的法院编号
        self.agency_code = agency_code
        # 对应的法院应用ID
        self.application_code = application_code
        # 业务类型标识
        self.business_type = business_type
        # 数据类型标识
        self.data_type = data_type
        # 地理位置信息
        self.location = location
        # 存证阶段
        self.phase = phase
        # 扩展属性
        self.properties = properties
        # 文本数据
        self.text_content = text_content
        # 存证事务ID
        self.transaction_id = transaction_id
        # 是否使用可信时间戳
        self.tsr = tsr

    def validate(self):
        if self.location:
            self.location.validate()
        self.validate_required(self.phase, 'phase')
        self.validate_required(self.text_content, 'text_content')
        self.validate_required(self.transaction_id, 'transaction_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.agency_code is not None:
            result['agency_code'] = self.agency_code
        if self.application_code is not None:
            result['application_code'] = self.application_code
        if self.business_type is not None:
            result['business_type'] = self.business_type
        if self.data_type is not None:
            result['data_type'] = self.data_type
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.properties is not None:
            result['properties'] = self.properties
        if self.text_content is not None:
            result['text_content'] = self.text_content
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.tsr is not None:
            result['tsr'] = self.tsr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('agency_code') is not None:
            self.agency_code = m.get('agency_code')
        if m.get('application_code') is not None:
            self.application_code = m.get('application_code')
        if m.get('business_type') is not None:
            self.business_type = m.get('business_type')
        if m.get('data_type') is not None:
            self.data_type = m.get('data_type')
        if m.get('location') is not None:
            temp_model = Location()
            self.location = temp_model.from_map(m['location'])
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('text_content') is not None:
            self.text_content = m.get('text_content')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('tsr') is not None:
            self.tsr = m.get('tsr')
        return self


class CreateCourtTextnotaryResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        tsr: TsrResponse = None,
        tx_hash: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 可信时间戳
        self.tsr = tsr
        # 交易哈希
        self.tx_hash = tx_hash

    def validate(self):
        if self.tsr:
            self.tsr.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.tsr is not None:
            result['tsr'] = self.tsr.to_map()
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('tsr') is not None:
            temp_model = TsrResponse()
            self.tsr = temp_model.from_map(m['tsr'])
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class GetCourtTextnotaryRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        location: Location = None,
        phase: str = None,
        properties: str = None,
        transaction_id: str = None,
        tx_hash: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 地理位置信息
        self.location = location
        # 存证阶段
        self.phase = phase
        # 扩展属性
        self.properties = properties
        # 存证事务ID
        self.transaction_id = transaction_id
        # 交易哈希
        self.tx_hash = tx_hash

    def validate(self):
        if self.location:
            self.location.validate()
        self.validate_required(self.tx_hash, 'tx_hash')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.properties is not None:
            result['properties'] = self.properties
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('location') is not None:
            temp_model = Location()
            self.location = temp_model.from_map(m['location'])
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class GetCourtTextnotaryResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        business_type: str = None,
        data_type: str = None,
        text_content: str = None,
        tsr: TsrResponse = None,
        agency_code: str = None,
        application_code: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务类型标识
        self.business_type = business_type
        # 数据类型标识
        self.data_type = data_type
        # 文本数据
        self.text_content = text_content
        # 可信时间戳
        self.tsr = tsr
        # 对应的法院编号
        self.agency_code = agency_code
        # 对应的法院应用ID
        self.application_code = application_code

    def validate(self):
        if self.tsr:
            self.tsr.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.business_type is not None:
            result['business_type'] = self.business_type
        if self.data_type is not None:
            result['data_type'] = self.data_type
        if self.text_content is not None:
            result['text_content'] = self.text_content
        if self.tsr is not None:
            result['tsr'] = self.tsr.to_map()
        if self.agency_code is not None:
            result['agency_code'] = self.agency_code
        if self.application_code is not None:
            result['application_code'] = self.application_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('business_type') is not None:
            self.business_type = m.get('business_type')
        if m.get('data_type') is not None:
            self.data_type = m.get('data_type')
        if m.get('text_content') is not None:
            self.text_content = m.get('text_content')
        if m.get('tsr') is not None:
            temp_model = TsrResponse()
            self.tsr = temp_model.from_map(m['tsr'])
        if m.get('agency_code') is not None:
            self.agency_code = m.get('agency_code')
        if m.get('application_code') is not None:
            self.application_code = m.get('application_code')
        return self


class CreateCourtFilenotaryRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        agency_code: str = None,
        application_code: str = None,
        business_type: str = None,
        data_type: str = None,
        file_hash: str = None,
        file_name: str = None,
        hash_algorithm: str = None,
        location: Location = None,
        phase: str = None,
        properties: str = None,
        transaction_id: str = None,
        tsr: bool = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 对应的法院编号
        self.agency_code = agency_code
        # 对应的法院应用ID
        self.application_code = application_code
        # 业务类型标识
        self.business_type = business_type
        # 数据类型标识
        self.data_type = data_type
        # 文件哈希
        self.file_hash = file_hash
        # 文件名
        self.file_name = file_name
        # 哈希算法，目前仅支持SHA256
        self.hash_algorithm = hash_algorithm
        # 地理位置信息
        self.location = location
        # 存证阶段
        self.phase = phase
        # 扩展属性
        self.properties = properties
        # 存证事务ID
        self.transaction_id = transaction_id
        # 是否使用可信时间戳
        self.tsr = tsr

    def validate(self):
        self.validate_required(self.file_hash, 'file_hash')
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.hash_algorithm, 'hash_algorithm')
        if self.location:
            self.location.validate()
        self.validate_required(self.phase, 'phase')
        self.validate_required(self.transaction_id, 'transaction_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.agency_code is not None:
            result['agency_code'] = self.agency_code
        if self.application_code is not None:
            result['application_code'] = self.application_code
        if self.business_type is not None:
            result['business_type'] = self.business_type
        if self.data_type is not None:
            result['data_type'] = self.data_type
        if self.file_hash is not None:
            result['file_hash'] = self.file_hash
        if self.file_name is not None:
            result['file_name'] = self.file_name
        if self.hash_algorithm is not None:
            result['hash_algorithm'] = self.hash_algorithm
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.properties is not None:
            result['properties'] = self.properties
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.tsr is not None:
            result['tsr'] = self.tsr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('agency_code') is not None:
            self.agency_code = m.get('agency_code')
        if m.get('application_code') is not None:
            self.application_code = m.get('application_code')
        if m.get('business_type') is not None:
            self.business_type = m.get('business_type')
        if m.get('data_type') is not None:
            self.data_type = m.get('data_type')
        if m.get('file_hash') is not None:
            self.file_hash = m.get('file_hash')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        if m.get('hash_algorithm') is not None:
            self.hash_algorithm = m.get('hash_algorithm')
        if m.get('location') is not None:
            temp_model = Location()
            self.location = temp_model.from_map(m['location'])
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('tsr') is not None:
            self.tsr = m.get('tsr')
        return self


class CreateCourtFilenotaryResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        tsr: TsrResponse = None,
        tx_hash: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 可信时间戳
        self.tsr = tsr
        # 交易哈希
        self.tx_hash = tx_hash

    def validate(self):
        if self.tsr:
            self.tsr.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.tsr is not None:
            result['tsr'] = self.tsr.to_map()
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('tsr') is not None:
            temp_model = TsrResponse()
            self.tsr = temp_model.from_map(m['tsr'])
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class GetCourtFilenotaryRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        location: Location = None,
        phase: str = None,
        properties: str = None,
        transaction_id: str = None,
        tx_hash: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 地理位置信息
        self.location = location
        # 存证阶段
        self.phase = phase
        # 扩展属性
        self.properties = properties
        # 存证事务ID
        self.transaction_id = transaction_id
        # 交易哈希
        self.tx_hash = tx_hash

    def validate(self):
        if self.location:
            self.location.validate()
        self.validate_required(self.tx_hash, 'tx_hash')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.properties is not None:
            result['properties'] = self.properties
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('location') is not None:
            temp_model = Location()
            self.location = temp_model.from_map(m['location'])
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class GetCourtFilenotaryResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        business_type: str = None,
        data_type: str = None,
        file_hash: str = None,
        file_name: str = None,
        tsr: TsrResponse = None,
        agency_code: str = None,
        application_code: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 业务类型标识
        self.business_type = business_type
        # 数据类型标识
        self.data_type = data_type
        # 文件哈希
        self.file_hash = file_hash
        # 文件名
        self.file_name = file_name
        # 可信时间戳
        self.tsr = tsr
        # 对应的法院编号
        self.agency_code = agency_code
        # 对应的法院应用ID
        self.application_code = application_code

    def validate(self):
        if self.tsr:
            self.tsr.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.business_type is not None:
            result['business_type'] = self.business_type
        if self.data_type is not None:
            result['data_type'] = self.data_type
        if self.file_hash is not None:
            result['file_hash'] = self.file_hash
        if self.file_name is not None:
            result['file_name'] = self.file_name
        if self.tsr is not None:
            result['tsr'] = self.tsr.to_map()
        if self.agency_code is not None:
            result['agency_code'] = self.agency_code
        if self.application_code is not None:
            result['application_code'] = self.application_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('business_type') is not None:
            self.business_type = m.get('business_type')
        if m.get('data_type') is not None:
            self.data_type = m.get('data_type')
        if m.get('file_hash') is not None:
            self.file_hash = m.get('file_hash')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        if m.get('tsr') is not None:
            temp_model = TsrResponse()
            self.tsr = temp_model.from_map(m['tsr'])
        if m.get('agency_code') is not None:
            self.agency_code = m.get('agency_code')
        if m.get('application_code') is not None:
            self.application_code = m.get('application_code')
        return self


class CreateLeaseRouteRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        route: str = None,
        biz_content: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 方法名
        self.route = route
        # 具体业务字段，json形式
        self.biz_content = biz_content

    def validate(self):
        self.validate_required(self.route, 'route')
        self.validate_required(self.biz_content, 'biz_content')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.route is not None:
            result['route'] = self.route
        if self.biz_content is not None:
            result['biz_content'] = self.biz_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('route') is not None:
            self.route = m.get('route')
        if m.get('biz_content') is not None:
            self.biz_content = m.get('biz_content')
        return self


class CreateLeaseRouteResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 状态码
        # 
        self.code = code
        # 错误信息
        # 
        self.err_message = err_message
        # 租方承诺信息存储到合约中对应的区块链交易哈希
        # 
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class QueryLeaseEncryptedinfoRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        lease_id: str = None,
        order_id: str = None,
        application_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 被查询的租赁公司对应的租户ID
        self.lease_id = lease_id
        # 订单id
        self.order_id = order_id
        # 融资租赁业务id，由资方控制台创建返回
        self.application_id = application_id

    def validate(self):
        self.validate_required(self.lease_id, 'lease_id')
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.lease_id is not None:
            result['lease_id'] = self.lease_id
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.application_id is not None:
            result['application_id'] = self.application_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('lease_id') is not None:
            self.lease_id = m.get('lease_id')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('application_id') is not None:
            self.application_id = m.get('application_id')
        return self


class QueryLeaseEncryptedinfoResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 错误码
        self.code = code
        # 错误描述信息
        self.err_message = err_message
        # 对应的加密后的具体信息
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class CreateContractTextRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        finish_info: ContractNotaryFinishInfo = None,
        flow_id: str = None,
        init_info: ContractNotaryInitInfo = None,
        phase: str = None,
        sign_info: ContractNotarySignInfo = None,
        transaction_id: str = None,
        document_info: ContractNotaryDocumentInfo = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 签署结束信息，phase为FINISH时必选
        self.finish_info = finish_info
        # 签署流程ID
        self.flow_id = flow_id
        # 签署发起信息，phase为INIT时必选
        self.init_info = init_info
        # 存证阶段，分为INIT(发起)，SIGN(签署)，FINISH(结束)
        self.phase = phase
        # 签署过程信息，phase为SIGN时必选
        self.sign_info = sign_info
        # 存证事务ID
        self.transaction_id = transaction_id
        # 签署文件存档阶段存证核验信息
        self.document_info = document_info

    def validate(self):
        if self.finish_info:
            self.finish_info.validate()
        self.validate_required(self.flow_id, 'flow_id')
        if self.init_info:
            self.init_info.validate()
        self.validate_required(self.phase, 'phase')
        if self.sign_info:
            self.sign_info.validate()
        self.validate_required(self.transaction_id, 'transaction_id')
        if self.document_info:
            self.document_info.validate()

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.finish_info is not None:
            result['finish_info'] = self.finish_info.to_map()
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.init_info is not None:
            result['init_info'] = self.init_info.to_map()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.sign_info is not None:
            result['sign_info'] = self.sign_info.to_map()
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.document_info is not None:
            result['document_info'] = self.document_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('finish_info') is not None:
            temp_model = ContractNotaryFinishInfo()
            self.finish_info = temp_model.from_map(m['finish_info'])
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('init_info') is not None:
            temp_model = ContractNotaryInitInfo()
            self.init_info = temp_model.from_map(m['init_info'])
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('sign_info') is not None:
            temp_model = ContractNotarySignInfo()
            self.sign_info = temp_model.from_map(m['sign_info'])
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('document_info') is not None:
            temp_model = ContractNotaryDocumentInfo()
            self.document_info = temp_model.from_map(m['document_info'])
        return self


class CreateContractTextResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        tx_hash: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 存证凭据
        self.tx_hash = tx_hash

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class ApplyContractReportRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        document_info: List[ContractNotaryDocumentInfo] = None,
        finish_info: ContractNotaryFinishInfo = None,
        flow_id: str = None,
        init_info: ContractNotaryInitInfo = None,
        sign_info: List[ContractNotarySignInfo] = None,
        transaction_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 签署文件存档阶段存证核验信息
        self.document_info = document_info
        # 签署结束阶段存证核验信息
        self.finish_info = finish_info
        # 签署流程ID
        self.flow_id = flow_id
        # 签署发起阶段存证核验信息
        self.init_info = init_info
        # 签署过程阶段存证核验信息
        self.sign_info = sign_info
        # 存证事务ID
        self.transaction_id = transaction_id

    def validate(self):
        if self.document_info:
            for k in self.document_info:
                if k:
                    k.validate()
        self.validate_required(self.finish_info, 'finish_info')
        if self.finish_info:
            self.finish_info.validate()
        self.validate_required(self.flow_id, 'flow_id')
        self.validate_required(self.init_info, 'init_info')
        if self.init_info:
            self.init_info.validate()
        self.validate_required(self.sign_info, 'sign_info')
        if self.sign_info:
            for k in self.sign_info:
                if k:
                    k.validate()
        self.validate_required(self.transaction_id, 'transaction_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        result['document_info'] = []
        if self.document_info is not None:
            for k in self.document_info:
                result['document_info'].append(k.to_map() if k else None)
        if self.finish_info is not None:
            result['finish_info'] = self.finish_info.to_map()
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.init_info is not None:
            result['init_info'] = self.init_info.to_map()
        result['sign_info'] = []
        if self.sign_info is not None:
            for k in self.sign_info:
                result['sign_info'].append(k.to_map() if k else None)
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        self.document_info = []
        if m.get('document_info') is not None:
            for k in m.get('document_info'):
                temp_model = ContractNotaryDocumentInfo()
                self.document_info.append(temp_model.from_map(k))
        if m.get('finish_info') is not None:
            temp_model = ContractNotaryFinishInfo()
            self.finish_info = temp_model.from_map(m['finish_info'])
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('init_info') is not None:
            temp_model = ContractNotaryInitInfo()
            self.init_info = temp_model.from_map(m['init_info'])
        self.sign_info = []
        if m.get('sign_info') is not None:
            for k in m.get('sign_info'):
                temp_model = ContractNotarySignInfo()
                self.sign_info.append(temp_model.from_map(k))
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        return self


class ApplyContractReportResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        auth_code: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 出证报告授权码，通过核验后获得
        self.auth_code = auth_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.auth_code is not None:
            result['auth_code'] = self.auth_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('auth_code') is not None:
            self.auth_code = m.get('auth_code')
        return self


class GetContractTextRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        tx_hash: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 存证凭据
        self.tx_hash = tx_hash

    def validate(self):
        self.validate_required(self.tx_hash, 'tx_hash')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class GetContractTextResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        notary_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 存证信息对象的JSON序列化形式
        self.notary_data = notary_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.notary_data is not None:
            result['notary_data'] = self.notary_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('notary_data') is not None:
            self.notary_data = m.get('notary_data')
        return self


class CreateInternalTransRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        customer: Identity = None,
        properties: str = None,
        sub_biz_id: str = None,
        tsr: bool = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 存证关联实体（个人/企业）的身份识别信息
        self.customer = customer
        # 扩展属性
        self.properties = properties
        # 业务子类型标识
        self.sub_biz_id = sub_biz_id
        # 是否使用可信时间戳，默认为false
        self.tsr = tsr

    def validate(self):
        self.validate_required(self.customer, 'customer')
        if self.customer:
            self.customer.validate()

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.customer is not None:
            result['customer'] = self.customer.to_map()
        if self.properties is not None:
            result['properties'] = self.properties
        if self.sub_biz_id is not None:
            result['sub_biz_id'] = self.sub_biz_id
        if self.tsr is not None:
            result['tsr'] = self.tsr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('customer') is not None:
            temp_model = Identity()
            self.customer = temp_model.from_map(m['customer'])
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('sub_biz_id') is not None:
            self.sub_biz_id = m.get('sub_biz_id')
        if m.get('tsr') is not None:
            self.tsr = m.get('tsr')
        return self


class CreateInternalTransResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        transaction_id: str = None,
        tsr: TsrResponse = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 返回事务ID，全局唯一
        self.transaction_id = transaction_id
        # 可信时间信息
        self.tsr = tsr

    def validate(self):
        if self.tsr:
            self.tsr.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.tsr is not None:
            result['tsr'] = self.tsr.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('tsr') is not None:
            temp_model = TsrResponse()
            self.tsr = temp_model.from_map(m['tsr'])
        return self


class CreateInternalTextRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        hash_algorithm: str = None,
        location: Location = None,
        notary_content: str = None,
        phase: str = None,
        properties: str = None,
        text_notary_type: str = None,
        transaction_id: str = None,
        tsr: bool = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 哈希算法，目前仅支持 SHA256
        self.hash_algorithm = hash_algorithm
        # 存证地点(如手机硬件ID，Wi-Fi地址，GPS位置，IP地址)
        self.location = location
        # 存证内容
        self.notary_content = notary_content
        # 描述本条存证在存证事务中的阶段，用户可自行维护
        self.phase = phase
        # 扩展属性
        self.properties = properties
        # 文本存证类型，支持源文本/文本哈希
        self.text_notary_type = text_notary_type
        # 存证事务id
        self.transaction_id = transaction_id
        # 是否使用可信时间戳，默认为false
        self.tsr = tsr

    def validate(self):
        if self.location:
            self.location.validate()
        self.validate_required(self.notary_content, 'notary_content')
        self.validate_required(self.phase, 'phase')
        self.validate_required(self.transaction_id, 'transaction_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.hash_algorithm is not None:
            result['hash_algorithm'] = self.hash_algorithm
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.notary_content is not None:
            result['notary_content'] = self.notary_content
        if self.phase is not None:
            result['phase'] = self.phase
        if self.properties is not None:
            result['properties'] = self.properties
        if self.text_notary_type is not None:
            result['text_notary_type'] = self.text_notary_type
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.tsr is not None:
            result['tsr'] = self.tsr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('hash_algorithm') is not None:
            self.hash_algorithm = m.get('hash_algorithm')
        if m.get('location') is not None:
            temp_model = Location()
            self.location = temp_model.from_map(m['location'])
        if m.get('notary_content') is not None:
            self.notary_content = m.get('notary_content')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('text_notary_type') is not None:
            self.text_notary_type = m.get('text_notary_type')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('tsr') is not None:
            self.tsr = m.get('tsr')
        return self


class CreateInternalTextResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        tsr: TsrResponse = None,
        tx_hash: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 可信时间信息
        self.tsr = tsr
        # 存证凭据
        self.tx_hash = tx_hash

    def validate(self):
        if self.tsr:
            self.tsr.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.tsr is not None:
            result['tsr'] = self.tsr.to_map()
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('tsr') is not None:
            temp_model = TsrResponse()
            self.tsr = temp_model.from_map(m['tsr'])
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class CreateLeaseTextRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        hash_algorithm: str = None,
        location: Location = None,
        notary_content: str = None,
        phase: str = None,
        properties: str = None,
        text_notary_type: str = None,
        transaction_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 哈希算法，目前仅支持 SHA256
        self.hash_algorithm = hash_algorithm
        # 存证地点(如手机硬件ID，Wi-Fi地址，GPS位置，IP地址)
        self.location = location
        # 存证内容
        self.notary_content = notary_content
        # 描述本条存证在存证事务中的阶段，用户可自行维护
        self.phase = phase
        # 扩展属性
        self.properties = properties
        # 文本存证类型，支持源文本/文本哈希
        self.text_notary_type = text_notary_type
        # 存证事务id
        self.transaction_id = transaction_id

    def validate(self):
        if self.location:
            self.location.validate()
        self.validate_required(self.notary_content, 'notary_content')
        self.validate_required(self.phase, 'phase')
        self.validate_required(self.transaction_id, 'transaction_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.hash_algorithm is not None:
            result['hash_algorithm'] = self.hash_algorithm
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.notary_content is not None:
            result['notary_content'] = self.notary_content
        if self.phase is not None:
            result['phase'] = self.phase
        if self.properties is not None:
            result['properties'] = self.properties
        if self.text_notary_type is not None:
            result['text_notary_type'] = self.text_notary_type
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('hash_algorithm') is not None:
            self.hash_algorithm = m.get('hash_algorithm')
        if m.get('location') is not None:
            temp_model = Location()
            self.location = temp_model.from_map(m['location'])
        if m.get('notary_content') is not None:
            self.notary_content = m.get('notary_content')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('text_notary_type') is not None:
            self.text_notary_type = m.get('text_notary_type')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        return self


class CreateLeaseTextResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        phase: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 入参中传入的存证阶段，可同用于租赁存证列表(twc.notary.lease.notary.list)的记录对账
        self.phase = phase

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.phase is not None:
            result['phase'] = self.phase
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        return self


class CreateLeaseFileRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        file_notary_type: str = None,
        hash_algorithm: str = None,
        location: Location = None,
        notary_file: str = None,
        notary_name: str = None,
        phase: str = None,
        properties: str = None,
        transaction_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 文件存证模式，目前仅支持 FILE_RAW 和 FILE_HASH
        self.file_notary_type = file_notary_type
        # 当文件存证模式为FILE_HASH时，用户可以指定该参数。当前服务仅支持 SHA256，若不填写，则默认值为 SHA256。
        self.hash_algorithm = hash_algorithm
        # 存证地点(如手机硬件ID，Wi-Fi地址，GPS位置，IP地址)
        self.location = location
        # 存证文件内容，对文件内容做base64编码后得到。例如FILE_RAW模式下，文件内容为“test”，那么base64编码后的结果则为“dGVzdA==”。如果是FILE_HASh模式，则该字段直接为文件hash。
        self.notary_file = notary_file
        # 存证文件名称
        self.notary_name = notary_name
        # 描述本条存证在存证事务中的阶段，用户可自行维护
        self.phase = phase
        # 扩展属性
        self.properties = properties
        # 存证事务ID
        self.transaction_id = transaction_id

    def validate(self):
        if self.location:
            self.location.validate()
        self.validate_required(self.notary_file, 'notary_file')
        self.validate_required(self.notary_name, 'notary_name')
        self.validate_required(self.phase, 'phase')
        self.validate_required(self.transaction_id, 'transaction_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.file_notary_type is not None:
            result['file_notary_type'] = self.file_notary_type
        if self.hash_algorithm is not None:
            result['hash_algorithm'] = self.hash_algorithm
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.notary_file is not None:
            result['notary_file'] = self.notary_file
        if self.notary_name is not None:
            result['notary_name'] = self.notary_name
        if self.phase is not None:
            result['phase'] = self.phase
        if self.properties is not None:
            result['properties'] = self.properties
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('file_notary_type') is not None:
            self.file_notary_type = m.get('file_notary_type')
        if m.get('hash_algorithm') is not None:
            self.hash_algorithm = m.get('hash_algorithm')
        if m.get('location') is not None:
            temp_model = Location()
            self.location = temp_model.from_map(m['location'])
        if m.get('notary_file') is not None:
            self.notary_file = m.get('notary_file')
        if m.get('notary_name') is not None:
            self.notary_name = m.get('notary_name')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        return self


class CreateLeaseFileResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        phase: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 入参中的存证阶段信息，可同用于租赁存证列表(twc.notary.lease.notary.list)的记录对账
        self.phase = phase

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.phase is not None:
            result['phase'] = self.phase
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        return self


class ListLeaseNotaryRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        merchant_order_no: str = None,
        order_no: str = None,
        payment_channel: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 商户订单号，需要同twc.notary.lease.order.create接口的传参一致
        self.merchant_order_no = merchant_order_no
        # 接口订单号，需要同twc.notary.lease.order.create接口的传参一致
        self.order_no = order_no
        # 支付渠道，默认支持Alipay|ThirdParty|CreditCard|BankTransfer|WeChatPay|Other，需要同twc.notary.lease.order.create接口的传参一致
        self.payment_channel = payment_channel

    def validate(self):
        self.validate_required(self.order_no, 'order_no')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.merchant_order_no is not None:
            result['merchant_order_no'] = self.merchant_order_no
        if self.order_no is not None:
            result['order_no'] = self.order_no
        if self.payment_channel is not None:
            result['payment_channel'] = self.payment_channel
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('merchant_order_no') is not None:
            self.merchant_order_no = m.get('merchant_order_no')
        if m.get('order_no') is not None:
            self.order_no = m.get('order_no')
        if m.get('payment_channel') is not None:
            self.payment_channel = m.get('payment_channel')
        return self


class ListLeaseNotaryResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        records: List[LeaseNotaryRecord] = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 存证记录列表
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        result['records'] = []
        if self.records is not None:
            for k in self.records:
                result['records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        self.records = []
        if m.get('records') is not None:
            for k in m.get('records'):
                temp_model = LeaseNotaryRecord()
                self.records.append(temp_model.from_map(k))
        return self


class QueryLeaseApplicationRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        page_size: int = None,
        start_id: int = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 每页的大小
        self.page_size = page_size
        # 起始id
        self.start_id = start_id

    def validate(self):
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.start_id, 'start_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.start_id is not None:
            result['start_id'] = self.start_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('start_id') is not None:
            self.start_id = m.get('start_id')
        return self


class QueryLeaseApplicationResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 错误码
        self.code = code
        # 错误描述
        self.err_message = err_message
        # 返回值
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class QueryLeaseApplicationdetailinfoRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        application_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 合约id
        self.application_id = application_id

    def validate(self):
        self.validate_required(self.application_id, 'application_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.application_id is not None:
            result['application_id'] = self.application_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('application_id') is not None:
            self.application_id = m.get('application_id')
        return self


class QueryLeaseApplicationdetailinfoResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 错误码
        self.code = code
        # 错误描述
        self.err_message = err_message
        # 合约定义详情
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class SetLeaseRepaymentstatusRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        lease_id: str = None,
        application_id: str = None,
        order_id: str = None,
        finish: int = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 租赁机构金融科技租户Id
        self.lease_id = lease_id
        # 融资租赁对应的合约id
        self.application_id = application_id
        # 融资租赁对应的订单id
        self.order_id = order_id
        # finish只能为0或1，0表示订单重置此状态下订单可以被再次操作【如清分记录上传、还款记录上传等】，1表示订单结束，在1的状态下不会再进行清分、还款记录上传等操作
        self.finish = finish

    def validate(self):
        self.validate_required(self.lease_id, 'lease_id')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.finish, 'finish')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.lease_id is not None:
            result['lease_id'] = self.lease_id
        if self.application_id is not None:
            result['application_id'] = self.application_id
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.finish is not None:
            result['finish'] = self.finish
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('lease_id') is not None:
            self.lease_id = m.get('lease_id')
        if m.get('application_id') is not None:
            self.application_id = m.get('application_id')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('finish') is not None:
            self.finish = m.get('finish')
        return self


class SetLeaseRepaymentstatusResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        response_data: str = None,
        code: int = None,
        err_message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 状态重置对应的链上交易哈希
        self.response_data = response_data
        # 状态码，0表示成功
        self.code = code
        # 错误信息描述
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.response_data is not None:
            result['response_data'] = self.response_data
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        return self


class CreateLeaseSupplierinfoRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        application_id: str = None,
        extra_info: str = None,
        logistics_order_id: str = None,
        order_id: str = None,
        phase: str = None,
        purchase_order_id: str = None,
        supplier_product_list: List[SupplierProductInfo] = None,
        maintained_by_supplier: int = None,
        deliver_time: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 租赁方及资方定义的合约id
        self.application_id = application_id
        # 额外字段定义
        self.extra_info = extra_info
        # 供应商发货的物流单号
        self.logistics_order_id = logistics_order_id
        # 用户的租赁订单id
        self.order_id = order_id
        # 额外字段定义对应的阶段，请咨询对应的资方
        self.phase = phase
        # 采购订单id
        self.purchase_order_id = purchase_order_id
        # 产品详细信息
        self.supplier_product_list = supplier_product_list
        # 1自有物流 2顺丰
        self.maintained_by_supplier = maintained_by_supplier
        # 发货时间
        self.deliver_time = deliver_time

    def validate(self):
        self.validate_required(self.application_id, 'application_id')
        self.validate_required(self.logistics_order_id, 'logistics_order_id')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.phase, 'phase')
        self.validate_required(self.purchase_order_id, 'purchase_order_id')
        self.validate_required(self.supplier_product_list, 'supplier_product_list')
        if self.supplier_product_list:
            for k in self.supplier_product_list:
                if k:
                    k.validate()
        self.validate_required(self.maintained_by_supplier, 'maintained_by_supplier')
        self.validate_required(self.deliver_time, 'deliver_time')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.application_id is not None:
            result['application_id'] = self.application_id
        if self.extra_info is not None:
            result['extra_info'] = self.extra_info
        if self.logistics_order_id is not None:
            result['logistics_order_id'] = self.logistics_order_id
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.phase is not None:
            result['phase'] = self.phase
        if self.purchase_order_id is not None:
            result['purchase_order_id'] = self.purchase_order_id
        result['supplier_product_list'] = []
        if self.supplier_product_list is not None:
            for k in self.supplier_product_list:
                result['supplier_product_list'].append(k.to_map() if k else None)
        if self.maintained_by_supplier is not None:
            result['maintained_by_supplier'] = self.maintained_by_supplier
        if self.deliver_time is not None:
            result['deliver_time'] = self.deliver_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('application_id') is not None:
            self.application_id = m.get('application_id')
        if m.get('extra_info') is not None:
            self.extra_info = m.get('extra_info')
        if m.get('logistics_order_id') is not None:
            self.logistics_order_id = m.get('logistics_order_id')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('purchase_order_id') is not None:
            self.purchase_order_id = m.get('purchase_order_id')
        self.supplier_product_list = []
        if m.get('supplier_product_list') is not None:
            for k in m.get('supplier_product_list'):
                temp_model = SupplierProductInfo()
                self.supplier_product_list.append(temp_model.from_map(k))
        if m.get('maintained_by_supplier') is not None:
            self.maintained_by_supplier = m.get('maintained_by_supplier')
        if m.get('deliver_time') is not None:
            self.deliver_time = m.get('deliver_time')
        return self


class CreateLeaseSupplierinfoResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 错误码，0表示成功
        self.code = code
        # 错误信息描述
        self.err_message = err_message
        # 供应商上传采购等相关信息对应的链上哈希
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class DeployMytfTappRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        tapp_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # tappId
        self.tapp_id = tapp_id

    def validate(self):
        self.validate_required(self.tapp_id, 'tapp_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.tapp_id is not None:
            result['tapp_id'] = self.tapp_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('tapp_id') is not None:
            self.tapp_id = m.get('tapp_id')
        return self


class DeployMytfTappResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        return self


class CreateLeaseSupplierdynamicinfoRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        application_id: str = None,
        arrive_confirm_hash: str = None,
        arrive_confirm_time: str = None,
        arrive_confirm_tx_hash: str = None,
        arrive_confirm_url: str = None,
        extra_info: str = None,
        logistic_status: str = None,
        order_id: str = None,
        phase: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 合约id
        self.application_id = application_id
        # 签收记录哈希，已签收需要必填
        self.arrive_confirm_hash = arrive_confirm_hash
        # 用户签收时间，格式为2019-8-31 12:00:00，已签收需要必填
        self.arrive_confirm_time = arrive_confirm_time
        # 签收记录存证哈希，已签收需要必填
        self.arrive_confirm_tx_hash = arrive_confirm_tx_hash
        # 签收记录对应的url，已签收需要必填
        self.arrive_confirm_url = arrive_confirm_url
        # 物流状态额外信息
        self.extra_info = extra_info
        # 物流状态，1.已发货 2运输中 3已签收 0其他
        self.logistic_status = logistic_status
        # 订单id
        self.order_id = order_id
        # 阶段名称
        self.phase = phase

    def validate(self):
        self.validate_required(self.application_id, 'application_id')
        self.validate_required(self.logistic_status, 'logistic_status')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.phase, 'phase')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.application_id is not None:
            result['application_id'] = self.application_id
        if self.arrive_confirm_hash is not None:
            result['arrive_confirm_hash'] = self.arrive_confirm_hash
        if self.arrive_confirm_time is not None:
            result['arrive_confirm_time'] = self.arrive_confirm_time
        if self.arrive_confirm_tx_hash is not None:
            result['arrive_confirm_tx_hash'] = self.arrive_confirm_tx_hash
        if self.arrive_confirm_url is not None:
            result['arrive_confirm_url'] = self.arrive_confirm_url
        if self.extra_info is not None:
            result['extra_info'] = self.extra_info
        if self.logistic_status is not None:
            result['logistic_status'] = self.logistic_status
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.phase is not None:
            result['phase'] = self.phase
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('application_id') is not None:
            self.application_id = m.get('application_id')
        if m.get('arrive_confirm_hash') is not None:
            self.arrive_confirm_hash = m.get('arrive_confirm_hash')
        if m.get('arrive_confirm_time') is not None:
            self.arrive_confirm_time = m.get('arrive_confirm_time')
        if m.get('arrive_confirm_tx_hash') is not None:
            self.arrive_confirm_tx_hash = m.get('arrive_confirm_tx_hash')
        if m.get('arrive_confirm_url') is not None:
            self.arrive_confirm_url = m.get('arrive_confirm_url')
        if m.get('extra_info') is not None:
            self.extra_info = m.get('extra_info')
        if m.get('logistic_status') is not None:
            self.logistic_status = m.get('logistic_status')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        return self


class CreateLeaseSupplierdynamicinfoResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 状态码
        self.code = code
        # 错误信息描述
        self.err_message = err_message
        # 链上哈希
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class CreateLeaseBizRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        biz_content: str = None,
        type: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 租赁订单相关内容，以json形式发送
        self.biz_content = biz_content
        # 租赁订单所属阶段
        self.type = type

    def validate(self):
        self.validate_required(self.biz_content, 'biz_content')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.biz_content is not None:
            result['biz_content'] = self.biz_content
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('biz_content') is not None:
            self.biz_content = m.get('biz_content')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateLeaseBizResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        response_data: str = None,
        code: str = None,
        err_message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 租赁信息上链后，链上对应的txHash
        self.response_data = response_data
        # 错误码
        self.code = code
        # 错误信息描述
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.response_data is not None:
            result['response_data'] = self.response_data
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        return self


class QueryLeaseProofRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        order_id: str = None,
        application_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 业务逻辑的订单id
        self.order_id = order_id
        # 2020
        self.application_id = application_id

    def validate(self):
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.application_id, 'application_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.application_id is not None:
            result['application_id'] = self.application_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('application_id') is not None:
            self.application_id = m.get('application_id')
        return self


class QueryLeaseProofResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 核验结果数据
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class CreateLargefileRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        file_id: str = None,
        location: Location = None,
        transaction_id: str = None,
        tsr: bool = None,
        notary_name: str = None,
        phase: str = None,
        properties: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 上传至中枢文件扩展服务后得到的文件ID
        self.file_id = file_id
        # 存证地点(如手机硬件ID，Wi-Fi地址，GPS位置，IP地址)
        self.location = location
        # 存证事务ID
        self.transaction_id = transaction_id
        # 是否使用可信时间戳，默认为false
        self.tsr = tsr
        # 存证文件名称
        self.notary_name = notary_name
        # 描述本条存证在存证事务中的阶段，用户可自行维护
        self.phase = phase
        # 扩展属性
        self.properties = properties

    def validate(self):
        self.validate_required(self.file_id, 'file_id')
        if self.location:
            self.location.validate()
        self.validate_required(self.transaction_id, 'transaction_id')
        self.validate_required(self.notary_name, 'notary_name')
        self.validate_required(self.phase, 'phase')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.location is not None:
            result['location'] = self.location.to_map()
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.tsr is not None:
            result['tsr'] = self.tsr
        if self.notary_name is not None:
            result['notary_name'] = self.notary_name
        if self.phase is not None:
            result['phase'] = self.phase
        if self.properties is not None:
            result['properties'] = self.properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('location') is not None:
            temp_model = Location()
            self.location = temp_model.from_map(m['location'])
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('tsr') is not None:
            self.tsr = m.get('tsr')
        if m.get('notary_name') is not None:
            self.notary_name = m.get('notary_name')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        return self


class CreateLargefileResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        tsr: TsrResponse = None,
        tx_hash: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 可信时间信息
        self.tsr = tsr
        # 存证凭证
        self.tx_hash = tx_hash

    def validate(self):
        if self.tsr:
            self.tsr.validate()

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.tsr is not None:
            result['tsr'] = self.tsr.to_map()
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('tsr') is not None:
            temp_model = TsrResponse()
            self.tsr = temp_model.from_map(m['tsr'])
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class QueryLeaseBizRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        biz_content: str = None,
        type: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 租赁订单相关内容，以json形式发送
        self.biz_content = biz_content
        # 租赁订单所属阶段
        self.type = type

    def validate(self):
        self.validate_required(self.biz_content, 'biz_content')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.biz_content is not None:
            result['biz_content'] = self.biz_content
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('biz_content') is not None:
            self.biz_content = m.get('biz_content')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class QueryLeaseBizResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 返回的查询值
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class CreateLeaseBiznotaryRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        hash: str = None,
        lease_corp_id: str = None,
        lease_corp_name: str = None,
        lease_corp_owner_name: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 要存证的文件哈希
        self.hash = hash
        # 租赁机构社会统一信用码
        self.lease_corp_id = lease_corp_id
        # 租赁机构公司名称
        self.lease_corp_name = lease_corp_name
        # 租赁机构法人姓名
        self.lease_corp_owner_name = lease_corp_owner_name

    def validate(self):
        self.validate_required(self.hash, 'hash')
        self.validate_required(self.lease_corp_id, 'lease_corp_id')
        self.validate_required(self.lease_corp_name, 'lease_corp_name')
        self.validate_required(self.lease_corp_owner_name, 'lease_corp_owner_name')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.hash is not None:
            result['hash'] = self.hash
        if self.lease_corp_id is not None:
            result['lease_corp_id'] = self.lease_corp_id
        if self.lease_corp_name is not None:
            result['lease_corp_name'] = self.lease_corp_name
        if self.lease_corp_owner_name is not None:
            result['lease_corp_owner_name'] = self.lease_corp_owner_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('hash') is not None:
            self.hash = m.get('hash')
        if m.get('lease_corp_id') is not None:
            self.lease_corp_id = m.get('lease_corp_id')
        if m.get('lease_corp_name') is not None:
            self.lease_corp_name = m.get('lease_corp_name')
        if m.get('lease_corp_owner_name') is not None:
            self.lease_corp_owner_name = m.get('lease_corp_owner_name')
        return self


class CreateLeaseBiznotaryResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        code: int = None,
        err_message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 是否租赁宝存证哈希成功，成功则为0，否则不为0
        self.code = code
        # 错误码具体详情
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.code is not None:
            result['code'] = self.code
        if self.err_message is not None:
            result['err_message'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        return self


class CreateInternalContractRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        finish_info: ContractNotaryFinishInfo = None,
        flow_id: str = None,
        init_info: ContractNotaryInitInfo = None,
        phase: str = None,
        sign_info: ContractNotarySignInfo = None,
        transaction_id: str = None,
        document_info: ContractNotaryDocumentInfo = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 签署结束信息，phase为FINISH时必选
        self.finish_info = finish_info
        # 签署流程ID
        self.flow_id = flow_id
        # 签署发起信息，phase为INIT时必选
        self.init_info = init_info
        # 存证阶段，分为INIT(发起)，SIGN(签署)，FINISH(结束)
        self.phase = phase
        # 签署过程信息，phase为SIGN时必选
        self.sign_info = sign_info
        # 存证事务ID
        self.transaction_id = transaction_id
        # 签署文件存档阶段存证核验信息
        self.document_info = document_info

    def validate(self):
        if self.finish_info:
            self.finish_info.validate()
        self.validate_required(self.flow_id, 'flow_id')
        if self.init_info:
            self.init_info.validate()
        self.validate_required(self.phase, 'phase')
        if self.sign_info:
            self.sign_info.validate()
        self.validate_required(self.transaction_id, 'transaction_id')
        if self.document_info:
            self.document_info.validate()

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.finish_info is not None:
            result['finish_info'] = self.finish_info.to_map()
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        if self.init_info is not None:
            result['init_info'] = self.init_info.to_map()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.sign_info is not None:
            result['sign_info'] = self.sign_info.to_map()
        if self.transaction_id is not None:
            result['transaction_id'] = self.transaction_id
        if self.document_info is not None:
            result['document_info'] = self.document_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('finish_info') is not None:
            temp_model = ContractNotaryFinishInfo()
            self.finish_info = temp_model.from_map(m['finish_info'])
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        if m.get('init_info') is not None:
            temp_model = ContractNotaryInitInfo()
            self.init_info = temp_model.from_map(m['init_info'])
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('sign_info') is not None:
            temp_model = ContractNotarySignInfo()
            self.sign_info = temp_model.from_map(m['sign_info'])
        if m.get('transaction_id') is not None:
            self.transaction_id = m.get('transaction_id')
        if m.get('document_info') is not None:
            temp_model = ContractNotaryDocumentInfo()
            self.document_info = temp_model.from_map(m['document_info'])
        return self


class CreateInternalContractResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        tx_hash: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 存证凭据
        self.tx_hash = tx_hash

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class CreateLeaseZftagreementsignRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        order_id: str = None,
        application_id: str = None,
        agreement_no: str = None,
        alipay_user_id: str = None,
        sign_time: str = None,
        valid_time: str = None,
        invalid_time: str = None,
        lease_id: str = None,
        agreement_status: int = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 订单id
        self.order_id = order_id
        # 合约id
        self.application_id = application_id
        # 网商直付通代扣协议号
        self.agreement_no = agreement_no
        # 实际签署协议的用户支付宝uid
        self.alipay_user_id = alipay_user_id
        # 签署时间
        self.sign_time = sign_time
        # 协议生效时间
        self.valid_time = valid_time
        # 协议失效时间
        self.invalid_time = invalid_time
        # 租赁方金融科技租户id
        self.lease_id = lease_id
        # 核验结果，1表示通过，-1表示不通过
        self.agreement_status = agreement_status

    def validate(self):
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.application_id, 'application_id')
        self.validate_required(self.agreement_no, 'agreement_no')
        self.validate_required(self.lease_id, 'lease_id')
        self.validate_required(self.agreement_status, 'agreement_status')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.application_id is not None:
            result['application_id'] = self.application_id
        if self.agreement_no is not None:
            result['agreement_no'] = self.agreement_no
        if self.alipay_user_id is not None:
            result['alipay_user_id'] = self.alipay_user_id
        if self.sign_time is not None:
            result['sign_time'] = self.sign_time
        if self.valid_time is not None:
            result['valid_time'] = self.valid_time
        if self.invalid_time is not None:
            result['invalid_time'] = self.invalid_time
        if self.lease_id is not None:
            result['lease_id'] = self.lease_id
        if self.agreement_status is not None:
            result['agreement_status'] = self.agreement_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('application_id') is not None:
            self.application_id = m.get('application_id')
        if m.get('agreement_no') is not None:
            self.agreement_no = m.get('agreement_no')
        if m.get('alipay_user_id') is not None:
            self.alipay_user_id = m.get('alipay_user_id')
        if m.get('sign_time') is not None:
            self.sign_time = m.get('sign_time')
        if m.get('valid_time') is not None:
            self.valid_time = m.get('valid_time')
        if m.get('invalid_time') is not None:
            self.invalid_time = m.get('invalid_time')
        if m.get('lease_id') is not None:
            self.lease_id = m.get('lease_id')
        if m.get('agreement_status') is not None:
            self.agreement_status = m.get('agreement_status')
        return self


class CreateLeaseZftagreementsignResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        err_message: str = None,
        code: int = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 错误码描述
        self.err_message = err_message
        # 错误码
        self.code = code
        # 协议上链哈希
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.code is not None:
            result['code'] = self.code
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class CreateLeaseZftagreementunsignRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        order_id: str = None,
        application_id: str = None,
        lease_id: str = None,
        agreement_no: str = None,
        unsign_time: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 订单id
        self.order_id = order_id
        # 合约id
        self.application_id = application_id
        # 租赁方金融科技租户id
        self.lease_id = lease_id
        # 直付通网商模式代扣协议号
        self.agreement_no = agreement_no
        # 直付通代扣协议解约时间
        self.unsign_time = unsign_time

    def validate(self):
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.application_id, 'application_id')
        self.validate_required(self.lease_id, 'lease_id')
        self.validate_required(self.agreement_no, 'agreement_no')
        self.validate_required(self.unsign_time, 'unsign_time')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.application_id is not None:
            result['application_id'] = self.application_id
        if self.lease_id is not None:
            result['lease_id'] = self.lease_id
        if self.agreement_no is not None:
            result['agreement_no'] = self.agreement_no
        if self.unsign_time is not None:
            result['unsign_time'] = self.unsign_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('application_id') is not None:
            self.application_id = m.get('application_id')
        if m.get('lease_id') is not None:
            self.lease_id = m.get('lease_id')
        if m.get('agreement_no') is not None:
            self.agreement_no = m.get('agreement_no')
        if m.get('unsign_time') is not None:
            self.unsign_time = m.get('unsign_time')
        return self


class CreateLeaseZftagreementunsignResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        err_message: str = None,
        code: int = None,
        response_data: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 错误码描述信息
        self.err_message = err_message
        # 错误码
        self.code = code
        # 网商直付通解约链上哈希
        self.response_data = response_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.err_message is not None:
            result['err_message'] = self.err_message
        if self.code is not None:
            result['code'] = self.code
        if self.response_data is not None:
            result['response_data'] = self.response_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('err_message') is not None:
            self.err_message = m.get('err_message')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('response_data') is not None:
            self.response_data = m.get('response_data')
        return self


class GetContractCertificateRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        flow_id: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 签署流程ID
        self.flow_id = flow_id

    def validate(self):
        self.validate_required(self.flow_id, 'flow_id')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.flow_id is not None:
            result['flow_id'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('flow_id') is not None:
            self.flow_id = m.get('flow_id')
        return self


class GetContractCertificateResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        url: str = None,
        code: int = None,
        message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 下载文件地址(一小时内有效)
        self.url = url
        # 状态值
        self.code = code
        # 状态信息描述
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.url is not None:
            result['url'] = self.url
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetCertificateDetailRequest(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        product_instance_id: str = None,
        tx_hash: str = None,
    ):
        # OAuth模式下的授权token
        self.auth_token = auth_token
        # 集群ID
        self.product_instance_id = product_instance_id
        # 存证哈希地址
        self.tx_hash = tx_hash

    def validate(self):
        self.validate_required(self.tx_hash, 'tx_hash')

    def to_map(self):
        result = dict()
        if self.auth_token is not None:
            result['auth_token'] = self.auth_token
        if self.product_instance_id is not None:
            result['product_instance_id'] = self.product_instance_id
        if self.tx_hash is not None:
            result['tx_hash'] = self.tx_hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auth_token') is not None:
            self.auth_token = m.get('auth_token')
        if m.get('product_instance_id') is not None:
            self.product_instance_id = m.get('product_instance_id')
        if m.get('tx_hash') is not None:
            self.tx_hash = m.get('tx_hash')
        return self


class GetCertificateDetailResponse(TeaModel):
    def __init__(
        self,
        req_msg_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        url: str = None,
        code: int = None,
        message: str = None,
    ):
        # 请求唯一ID，用于链路跟踪和问题排查
        self.req_msg_id = req_msg_id
        # 异常信息的文本描述
        self.result_code = result_code
        self.result_msg = result_msg
        # 存证证明下载地址
        self.url = url
        # 状态值
        self.code = code
        # 状态信息描述
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.req_msg_id is not None:
            result['req_msg_id'] = self.req_msg_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.url is not None:
            result['url'] = self.url
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('req_msg_id') is not None:
            self.req_msg_id = m.get('req_msg_id')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


