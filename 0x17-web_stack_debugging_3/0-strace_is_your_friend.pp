# fix file of wp
file_line {'fix-wp':
  ensure            => present,
  path              => '/var/www/html/wp-settings.php',
  line              => "require_once( ABSPATH . WPINC . '/class-wp-locale.php' );",
  match             => "require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );",
  match_for_absence => true,
}