# Test Django project: use unit tests & custom user model

## Custom user model that uses email instead of username

- Custom user model based on AbstractUser class.

- Custom user manager based on CustomUserManager class; replaces two methods:

  - create_user
  - create_superuser
    - is_staff = True
    - is_superuser = True

---

## Unit tests

- Pages uses the SimpleTestCase class to build unit tests that do not access the DB:
  - url_exists_at_correct_location
  - url_available_by_name
  - template_name_correct
  - template_content

- Posts uses the TestCase class to test DB-related and non-related functionality:
  - model_content
  - url_at_correct_location
  - url_available_by_name
  - template_name_correct
  - template_content
  
- Users tests with TestCase:
  - create_user
    - record has correct email
    - user.is_active
    - user.is_staff false
    - user.is_superuser false
    - username is none
  
  - create_superuser
    - record has correct email
    - user.is_active
    - user.is_staff
    - user.is_superuser
    - username is none
    
---