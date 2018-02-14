# Homepage for http://realfast.io

This repo is home all content for the *realfast* project homepage. Included is a lightweight content manager written in Python and instructions for setting up this website on a server.

## Installation
Our web server is configured in the following way (as of 02/14/2018):
1. Install NGINX and Python (including Flask and gunicorn)
2. Clone this repository to `/data/www`
3. Clone [this repo](https://github.com/realfastvla/realfast.io-news) to `/data/news` 
4. Start a gunicorn server for the news app on some high-level port (say, for example, `1234`)
5. Configure NGINX in the following way (minimally)
```
http {
    server {
        listen 80;
        server_name realfast.io;

        location / {
            root /data/www;
            include /etc/nginx/mime.types;
        }

        location /news/ {
            proxy_pass http://127.0.0.1:1234;
            proxy_set_header Host $host;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }
}
```

## Adding content
Some of the simpler aspects of this website can be edited in place using the lightweight content manager located in `content/gen_content.py`. This content manager assumes a directory structure as explained in the installation section of this README. Editable/Addable components are
 - **About** page: editable using markdown syntax
 - **Data** page: can add cards to this page by adding entries to `content/data.json`
 - **Services** page: can add cards to this page by adding entries to `content/services.json`
 - **Sofware** page: can add cards to this page by adding entries to `content/software.json`
 - **Thanks** page: editable using markdow syntax
 - can add news items (which appear as news cards on the homepage) using markdown syntax
Images which must appear on each page can be added to the appropriate `content/*_images` directory. As of this writing, news items cannot contain images.

Build `.html` files and put content in the appropriate place for the web server to find by running the `content/gen_content.py` script.

