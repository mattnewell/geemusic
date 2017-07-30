from geemusic import app
import os
from LoggingMiddleware import LoggingMiddleware
from OpenSSL import SSL

# context = SSL.Context(SSL.TLSv1_2_METHOD)
# context.use_privatekey_file('/etc/letsencrypt/live/geemusic.burkenweb.com/privkey.pem')
# context.use_certificate_file('/etc/letsencrypt/live/geemusic.burkenweb.com/cert.pem')

if __name__ == '__main__':
    app.config['ASK_VERIFY_REQUESTS'] = False
    context = ('/etc/letsencrypt/live/geemusic.burkenweb.com/fullchain.pem', '/etc/letsencrypt/live/geemusic.burkenweb.com/privkey.pem')

#    port = int(os.environ.get("PORT", 443))
    app.wsgi_app = LoggingMiddleware(app.wsgi_app)
    app.run(host='0.0.0.0', port=443, debug=True, ssl_context=context)
