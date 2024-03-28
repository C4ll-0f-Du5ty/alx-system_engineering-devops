# installing Flask using Puppet
package { 'flask':
  ensure   => installed,
}

package { 'Werkzeug':
  ensure   => '2.1.1'
  provider => 'pip3'
}

package { 'Python':
  ensure => installed
}

exec { 'ACTION':
  command => '/usr/bin/pip3 install flask=2.1.0',
  path    => ['/usr/bin/', '/usr/sbin/'],
  require => [package['Werkzeug'], package['python3']],
}
