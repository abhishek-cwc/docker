Magento2 Instalation:
------------------------------
sudo su
1. docker-compose up --build
2. docker exec -it container_id bash
3. composer install
4. php bin/magento setup:install \
--base-url=http://local.domain.com/ \
--db-host=mysql \
--db-name=magento2.4.5 \
--db-user=root \
--db-password=root \
--admin-firstname=Admin \
--admin-lastname=User \
--admin-email=admin@example.com \
--admin-user=admin \
--admin-password=Admin123! \
--language=en_US \
--currency=USD \
--timezone=America/Chicago \
--use-rewrites=1 \
--search-engine=elasticsearch7 \
--elasticsearch-host=elasticsearch \
--elasticsearch-port=9200

Node Js Using Docker :
-------------------------



