import request from './request'

export function updatePassword(data) {
  return request({ url: '/users/password', method: 'put', data })
}
