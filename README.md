# Test task for vacancy

Test project for online store https://mega.readyscript.ru/

Contain 4 tests:
* test_user_login
* test_show_tablet_digma
* test_add_item_to_cart_and_delete
* test_add_item_to_favorite_and_delete


# Running tests in Docker

To run the tests in Docker, ensure that Docker is installed on your system. Then, execute the following commands:

1. Build the Docker image:
   ```bash
   docker build -t test_task_for_vacancy .
   
2. Run the container:
   ```bash
   docker run test_task_for_vacancy
