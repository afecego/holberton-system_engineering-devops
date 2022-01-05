# ssh configuration file for the local SSH client whit puppet
file_line { 'Declare identity file':
    ensure => created,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
}

file_line { '>Turn off passwd auth':
    ensure => created,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
}
