from fastapi import APIRouter, UploadFile, File, Depends

from fastapi.responses import StreamingResponse

from workshop.services.auth import get_current_user
from workshop.services.reports import ReportService
from workshop.tables import User

router = APIRouter(
    prefix='/reports'
)


@router.post('/import')
def import_csv(
        file: UploadFile = File(...),
        user: User = Depends(get_current_user),
        report_service: ReportService = Depends()
):
    report_service.import_csv(
        user_id=user.id,
        file=file.file
    )


@router.post('/export')
def export_csv(
        user: User = Depends(get_current_user),
        report_service: ReportService = Depends()
):
    report = report_service.export_csv(user.id)
    return StreamingResponse(
        report,
        media_type='text/csv',
        headers={
            'Content-Disposition': 'attachment; filename=report.csv'
        }
    )


@router.get('/')
def test():
    return {"test": "Hello world"}