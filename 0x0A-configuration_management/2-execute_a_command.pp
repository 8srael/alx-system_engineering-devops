# Kill a process named 'killmenow'
# Requirements:
# Must use the 'exec' Puppet resource
# Must use 'pkill' bash command


exec { 'kill-process-killmenow' :
  command => '/usr/bin/pkill -f killmenow',
  user    => 'root',
}
