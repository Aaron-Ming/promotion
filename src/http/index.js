import axios from 'axios'

const qs = require('qs')

const instance = axios.create({
  validateStatus (status) {
    return status >= 200 && status <= 500
  },
  transformRequest: [function(data){
    data = qs.stringify(data)
    return data
  }],
  timeout: 5000,
})

instance.defaults.xsrfHeaderName = 'X-CSRFToken'
instance.defaults.xsrfCookieName = 'csrftoken'

export default instance