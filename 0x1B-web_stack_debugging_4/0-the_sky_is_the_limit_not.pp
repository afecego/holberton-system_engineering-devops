# fix Failed requests
exec {'fix-failed_requests':
  command => 'sed -i s/15/4096/g /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'restart_nginx':
  command => 'service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  require => Exec ['fix-failed_requests']
}
