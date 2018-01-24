import axios from 'axios'

const instance = axios.create({
  validateStatus (status) {
    return status >= 200 && status <= 500
  },
  timeout: 5000,
})

export default instance