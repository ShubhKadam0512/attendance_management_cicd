from fastapi import APIRouter, Depends

from app.core.security import require_role


router = APIRouter(
    prefix="/rbac",
    tags=["Role-Based Access Control"]
)


@router.get("/system-admin")
def system_admin_test(
    current_user: dict = Depends(
        require_role("system_admin")
    )
):
    return {
        "message": "System Admin access granted",
        "user": current_user
    }


@router.get("/college-admin")
def college_admin_test(
    current_user: dict = Depends(
        require_role("college_admin")
    )
):
    return {
        "message": "College Admin access granted",
        "user": current_user
    }


@router.get("/faculty")
def faculty_test(
    current_user: dict = Depends(
        require_role("faculty")
    )
):
    return {
        "message": "Faculty access granted",
        "user": current_user
    }


@router.get("/student")
def student_test(
    current_user: dict = Depends(
        require_role("student")
    )
):
    return {
        "message": "Student access granted",
        "user": current_user
    }