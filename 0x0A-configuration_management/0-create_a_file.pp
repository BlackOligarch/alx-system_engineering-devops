# This manifest creates a file 'school' in 'tmp' directory

file {'/tmp/school':
  ensure  => present,
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
