# -*- coding: utf-8 -*-
"""全局常量"""
# 数据错误
BAD_REQUEST = 400  # 请求信息不完整或无法解析。
INVALID_REQUEST = 422  # 请求信息完整，但无效。
RESOURCE_NOT_FOUND = 404  # 资源不存在。
RESOURCE_CONFLICT = 409  # 资源冲突。

# 鉴权错误
INVALID_TOKEN = 401  # 访问令牌没有提供，或者无效。
FORBIDDEN = 403  # 访问令牌有效，但没有权限。

# 标准状态
INTERNAL_ERROR = 500  # 服务器内部抛出错误。

SUCCESS_MESSAGE = 'OK'
