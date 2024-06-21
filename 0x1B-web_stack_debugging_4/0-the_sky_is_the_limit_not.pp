exec { 'nginx-limit-fix':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => ['/sbin', '/usr/sbin', '/bin', '/usr/bin'],
  require => Exec['nginx-limit-fix'],
}
