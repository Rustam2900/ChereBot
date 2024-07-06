from aiogram import Router
from .start import router as start_router
from .cancel import router as cancel_router
from .products import router as products_router

router = Router()
router.include_router(cancel_router)
router.include_router(start_router)
router.include_router(products_router)

__all__ = [
    "router"
]
