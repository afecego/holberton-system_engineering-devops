# fix file of wp
exec {'fix-wp':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ':/usr/share/php:/usr/share/pear',
}