# fix file of wp
file_line {'fix-wp':
  command   => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path      => ':/usr/share/php:/usr/share/pear',
}