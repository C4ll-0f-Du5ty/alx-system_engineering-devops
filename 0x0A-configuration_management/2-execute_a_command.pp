# Killing a process usng Puppet
exec { 'kill':
  command => 'pkill -f killmenow',
  path    => '/user/bin',
}
