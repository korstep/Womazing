export function validateName(name) {
  const regexName = /^[a-zA-Z]{1,16}$/
  return regexName.test(name)
}

export function validatePhone(phone) {
  const regexPhone = /^(?:\+38)?[0-9]{9}$/
  return regexPhone.test(phone)
}
