import request from './request'

export function getFileList() {
  return request({ url: '/files', method: 'get' })
}

export function deleteFile(id) {
  return request({ url: `/files/${id}`, method: 'delete' })
}
