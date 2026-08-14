# attendance_management_cicd
#complete authentication flow

                FRONTEND
                   │
                   │ Register
                   ▼
          POST /auth/register
                   │
                   ▼
               FastAPI
                   │
                   ▼
           Validate with Pydantic
                   │
                   ▼
          Hash password with bcrypt
                   │
                   ▼
             SQLAlchemy
                   │
                   ▼
              PostgreSQL

#For login:

               FRONTEND
                   │
                   │ Email + Password
                   ▼
            POST /auth/login
                   │
                   ▼
               FastAPI
                   │
                   ▼
        Find user by email
                   │
                   ▼
     Verify bcrypt password hash
                   │
             ┌─────┴─────┐
             │           │
           Wrong       Correct
             │           │
             ▼           ▼
          401 Error    Create JWT
                           │
                           ▼
                    Send JWT to frontend
#Then for protected APIs:

                 Frontend
                   │
                   │ Authorization: Bearer JWT
                   ▼
                FastAPI
                   │
                   ▼
                Validate JWT
                   │
                   ▼
                Get user ID from "sub"
                   │
                   ▼
                Find user in PostgreSQL
                   │
                   ▼
                Allow protected operation
