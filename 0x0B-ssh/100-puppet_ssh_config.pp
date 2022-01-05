# SSH configuration file for the local SSH client whit puppet
file_line { 'Declare_identity_file':
    ensure => created,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
}

file_line { 'Turn_off_passwd_auth':
    ensure => created,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
}
