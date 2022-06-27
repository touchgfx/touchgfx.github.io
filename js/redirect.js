let newest_version = "4.20"

if (window && window.location) {
  let version_regex = /^(\/[0-9]+.[0-9]+)/
  let path = window.location.pathname
  let new_path = (path.endsWith('/') && path !== '/') ? path.substr(0, path.length - 1) : path
  let match = new_path.match(version_regex)

  if (match == null)
  {
    new_path = "/" + newest_version + new_path
  }

  if (new_path !== path)
  {
    window.location.replace(new_path + window.location.hash)
  }
}
