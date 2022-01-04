# manifest that kills a process
exec { 'killmenow':
    command => 'pkill -15 killmenow',
    path    => '/usr/local/bin/:/bin/',
}