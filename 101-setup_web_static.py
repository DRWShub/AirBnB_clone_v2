#Puppet file to configure nginx web server
#Configuration file
$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root /var/www/html;
    index index.html index.htm;

    location /redirect_me {
        return 301 https://youtube.com;
    }

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
   
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
} ->

file { '/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
} ->

file { '/data/web_static':
  ensure  => 'directory'
} ->

file { '/data/web_static/releases':
  ensure  => 'directory'
} ->

file { '/data/web_static/releases/test':
  ensure  => 'directory'
} ->

file { '/data/web_static/shared':
  ensure  => 'directory'
} ->

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => '<html>
                 <head>
                 </head>
                 <body>
                   Holberton School
                 </body>
               </html>',
} ->

file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test'
} ->

file { '/var/www':
  ensure  => 'directory'
} ->

file { '/var/www/html':
  ensure  => 'directory'
} ->

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => '<html>
                 <head>
                 </head>
                 <body>
                   Holberton School
                </body>
               </html>',
} ->

file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page"
} ->

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf
} ->

exec { 'nginx restart':
  path => '/etc/init.d/'
}
