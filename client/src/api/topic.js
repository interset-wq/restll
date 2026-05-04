import request from '@/utils/request'

/********/
/* User */
/********/

// List View
export const getMyTopics = () => {
  return request({
    url: '/topics',
    method: 'get',
  })
}

// Detail View
export const getMyTopicDetail = (id) => {
  return request({
    url: `/topics/${id}`,
    method: 'get',
  })
}

// New Topic
export const createMyTopic = (data) => {
  return request({
    url: '/topics',
    method: 'post',
    data: data,
  })
}

// Update entirely
export const updateMyTopic = (id, data) => {
  return request({
    url: `/topics/${id}`,
    method: 'put',
    data: data,
  })
}

// Update partly
export const patchMyTopic = (id, data) => {
  return request({
    url: `/topics/${id}`,
    method: 'patch',
    data: data,
  })
}

// Delete
export const deleteMyTopic = (id) => {
  return request({
    url: `/topics/${id}`,
    method: 'delete',
  })
}
