# Install a package
package { 'puppet-lint':
    ensure   => ['2.5.2', '2.4.2'],
    provider => 'gem',
}