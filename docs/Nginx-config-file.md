```
server {
    listen 5800;
    server_name _;

    #access_log /home/pi/git/FRC-2018/logs/nginx-access.log;
    error_log  /home/pi/git/FRC-2018/logs/nginx-errors.log;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_redirect     off;

        rewrite ^/$ /image?delay=0.25 permanent;

        proxy_set_header   Host                 $host;
        proxy_set_header   X-Real-IP            $remote_addr;
        proxy_set_header   X-Forwarded-For      $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto    $scheme;
    }
}
```