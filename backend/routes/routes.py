from fastapi import APIRouter, Depends, HTTPException, status, Query
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List, Optional
import logging
from datetime import datetime
 
# --- Controllers de Abel ---
# from controllers.album_controller import AlbumControllers
# from controllers.auth_controller import AuthControllers
# from controllers.inventory_controller import InventoryControllers
# from controllers.order_controller import OrderControllers
# from controllers.review_controller import ReviewControllers
from schemas.album_schema import AlbumCreate, AlbumUpdate, AlbumResponse
from schemas.auth_schema import LoginSchema, TokenSchema
from schemas.user_schema import UserCreate, UserResponse
from schemas.order_schema import OrderCreate, OrderResponse
# TODO: Maria necesita crear InventorySchema (product_inventory)
# TODO: Maria necesita crear ReviewSchema (reviews)
 
from database.database import get_db
 

logger = logging.getLogger(__name__)


router_albums    = APIRouter(prefix="/api/v1/albums",    tags=["albums"])
router_inventory = APIRouter(prefix="/api/v1/inventory", tags=["inventory"])
router_auth      = APIRouter(prefix="/api/v1/auth",      tags=["auth"])
router_orders    = APIRouter(prefix="/api/v1/orders",    tags=["orders"])
router_reviews   = APIRouter(prefix="/api/v1/reviews",   tags=["reviews"])
 

 
@router_albums.get(
    "/",
    response_model=List[AlbumResponse],
    status_code=status.HTTP_200_OK,
    summary="Obtener catálogo de álbumes",
    description=(
        "Lista paginada de álbumes. "
        "Filtros por género, artista y formato. "
        "Búsqueda por texto con ?search=. "
        "HU-03 + HU-05."
    )
)
def get_albums(
    genre:   Optional[str] = Query(None, description="Filtrar por genre (Genre.name)"),
    artist:  Optional[str] = Query(None, description="Filtrar por artist (Artist.name)"),
    format:  Optional[str] = Query(None, description="Filtrar por format (CD, Vinilo, Cassette)"),
    search:  Optional[str] = Query(None, description="Búsqueda parcial en title y artist"),
    page:    int = Query(1,  ge=1,         description="Número de página"),
    limit:   int = Query(20, ge=1, le=100, description="Ítems por página (máx. 100)"),
    db: Session = Depends(get_db)
):
    # TODO: return AlbumControllers.get_albums(db, genre, artist, format, search, page, limit)
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail="Controller pendiente de Abel"
    )
 
 
@router_albums.get(
    "/{album_id}",
    response_model=AlbumResponse,
    status_code=status.HTTP_200_OK,
    summary="Obtener detalle de un álbum",
    description=(
        "Devuelve un álbum por ID con sus formatos y stock. "
        "HU-04."
    )
)
def get_album_by_id(
    album_id: int,
    db: Session = Depends(get_db)
):
    # TODO: album = AlbumControllers.get_album_by_id(db, album_id)
    album = None  # placeholder
    if album is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Album with id {album_id} not found"
        )
    return album
 
 
@router_albums.post(
    "/",
    response_model=AlbumResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear álbum (admin)",
    description=(
        "Crea un álbum nuevo. image_url se recibe como URL en el body. "
        "HU-06."
    )
    # TODO HU-10  Depends(verify_admin) cuando Abel entregue verify_token
)
def create_album(
    album: AlbumCreate,
    db: Session = Depends(get_db)
    # TODO HU-10: current_user = Depends(verify_admin)
):
    # TODO: return AlbumControllers.create_album(db, album)
    # NOTA: AlbumCreate tiene category_id pero Album en models no tiene esa columna
    # TODO: resolver discrepancia models y schemas
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail="Controller pendiente de Abel"
    )
 
 
@router_albums.patch(
    "/{album_id}",
    response_model=AlbumResponse,
    status_code=status.HTTP_200_OK,
    summary="Actualizar álbum parcialmente (admin)",
    description=(
        "Actualiza solo los campos enviados. "
        "Registra cambios con logger.info(). "
        "HU-08."
    )
    # TODO HU-10: añadir Depends(verify_admin)
)
def update_album(
    album_id: int,
    album: AlbumUpdate,
    db: Session = Depends(get_db)
    # TODO HU-10: current_user = Depends(verify_admin)
):
    # TODO: updated = AlbumControllers.update_album(db, album_id, album)
    updated = None  # placeholder
    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Album with id {album_id} not found"
        )
    logger.info(
        f"[{datetime.now()}] Album {album_id} updated — "
        f"fields: {album.model_dump(exclude_none=True)}"
    )
    return updated
 
 
 
@router_inventory.post(
    "/",
    # TODO: response_model=InventoryResponse —  crear este schema
    status_code=status.HTTP_201_CREATED,
    summary="Añadir formato/stock a un álbum (admin)",
    description=(
        "Añade una fila a product_inventory. "
        "Campos: album_id, format_type, barcode, price, stock. "
        "Devuelve 409 si barcode ya existe. "
        "HU-07."
    )
    # TODO HU-10: añadir Depends(verify_admin)
)
def create_inventory(
    # TODO: inventory: InventoryCreate —  crear este schema
    db: Session = Depends(get_db)
    # TODO HU-10: current_user = Depends(verify_admin)
):
    # TODO: result = InventoryControllers.create_inventory(db, inventory)
    # Si barcode duplicado → 409
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail="InventorySchema pendiente de Maria + controller de Abel"
    )
 
 
@router_inventory.patch(
    "/{inventory_id}",
    # TODO: response_model=InventoryResponse
    status_code=status.HTTP_200_OK,
    summary="Actualizar stock/precio de un formato (admin)",
    description=(
        "Actualiza solo los campos enviados. "
        "Devuelve 400 si stock quedaría negativo. "
        "Registra cambios con logger.info(). "
        "HU-08."
    )
    # TODO HU-10: añadir Depends(verify_admin)
)
def update_inventory(
    inventory_id: int,
    # TODO: inventory: InventoryUpdate —  crear este schema
    db: Session = Depends(get_db)
    # TODO HU-10: current_user = Depends(verify_admin)
):
    # TODO: updated = InventoryControllers.update_inventory(db, inventory_id, inventory)
    updated = None  # placeholder
    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Inventory item with id {inventory_id} not found"
        )

    logger.info(
        f"[{datetime.now()}] Inventory {inventory_id} updated"
        # TODO: añadir campos cuando exista InventoryUpdate schema
    )
    return updated
 
 
@router_inventory.get(
    "/export",
    status_code=status.HTTP_200_OK,
    summary="Exportar inventario a CSV (admin)",
    description=(
        "Descarga el inventario como CSV. "
        "Nombre del archivo: inventory_YYYY-MM-DD.csv. "
        "Filtro opcional por format_type. "
        "HU-09."
    )
    # TODO HU-10: añadir Depends(verify_admin)
)
def export_inventory_csv(
    format_type: Optional[str] = Query(None, description="Filtrar por format_type (opcional)"),
    db: Session = Depends(get_db)
    # TODO HU-10: current_user = Depends(verify_admin)
):
    # Se genera el CSV, routes.py lo devuelve con FileResponse
    fecha = datetime.now().strftime("%Y-%m-%d")
    filename = f"inventory_{fecha}.csv"
    # TODO: csv_path = InventoryControllers.generate_csv(db, format_type)
    # TODO: descomentar cuando exista:
    # return FileResponse(path=csv_path, media_type="text/csv", filename=filename)
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail="Controller CSV pendiente de Abel"
    )
 
 
# ===========================================================================
# AUTH
# HU-12 — Registro → POST /auth/register
# HU-13 — Login    → POST /auth/login
# Tabla: user (User en models.py, campo role para JWT)
# ===========================================================================
 
@router_auth.post(
    "/register",
    response_model=TokenSchema,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar usuario",
    description=(
        "Crea un User nuevo. "
        "Email duplicado devuelve 409. "
        "Abel hace bcrypt + genera JWT. "
        "HU-12."
    )
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    # TODO: result = AuthControllers.register(db, user)
    result = None  # placeholder
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An account with this email already exists"
        )
    return result
 
 
@router_auth.post(
    "/login",
    response_model=TokenSchema,
    status_code=status.HTTP_200_OK,
    summary="Login de usuario",
    description=(
        "Verifica credenciales. "
        "Devuelve JWT con User.role y expiración 24h. "
        "HU-13."
    )
)
def login(
    credentials: LoginSchema,
    db: Session = Depends(get_db)
):
    # TODO: result = AuthControllers.login(db, credentials)
    # Abel verifica bcrypt(password) contra User.password_hash
    # JWT incluye User.role (customer / admin)
    result = None  # placeholder
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    return result
 
 
# ===========================================================================
# ORDERS
# HU-14 — Realizar pedido      → POST /orders
# HU-15 — Ver mis pedidos      → GET /orders/me
# HU-16 — Cambiar estado admin → PATCH /orders/{id}/status
# Tablas: orders + order_details en models.py
# ===========================================================================
 
@router_orders.post(
    "/",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Realizar pedido",
    description=(
        "Crea un pedido con lista de álbumes y cantidades. "
        "Requiere token. Verifica stock y calcula total_price. "
        "HU-14."
    )
    # TODO HU-10: añadir Depends(verify_token)
)
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db)
    # TODO HU-13: current_user = Depends(verify_token)
):
    # TODO: result = OrderControllers.create_order(db, order, user_id=current_user.id)
    # NOTA: OrderResponse tiene 'items' pero Orders en models no tiene
    # relationship definido todavía
    # TODO: resolver con Naimireth — añadir relationship Orders → order_details
    result = None  # placeholder
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient stock for one or more items"
        )
    return result
 
 
@router_orders.get(
    "/me",
    response_model=List[OrderResponse],
    status_code=status.HTTP_200_OK,
    summary="Ver mis pedidos",
    description=(
        "Devuelve los pedidos del usuario autenticado "
        "ordenados por order_date descendente. "
        "user_id se extrae del token, no de la URL. "
        "HU-15."
    )
    # TODO HU-10: añadir Depends(verify_token)
)
def get_my_orders(
    db: Session = Depends(get_db)
    # TODO HU-13: current_user = Depends(verify_token)
):
    # TODO: return OrderControllers.get_orders_by_user(db, user_id=current_user.id)
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail="Token pendiente de Abel"
    )
 
 
@router_orders.patch(
    "/{order_id}/status",
    response_model=OrderResponse,
    status_code=status.HTTP_200_OK,
    summary="Cambiar estado de pedido (admin)",
    description=(
        "Solo admins. Cambia Orders.order_status. "
        "Bloquea retroceso desde 'delivered'. "
        "HU-16."
    )
    # TODO HU-10: añadir Depends(verify_admin)
)
def update_order_status(
    order_id: int,
    new_status: str = Query(..., description="Nuevo valor de order_status"),
    db: Session = Depends(get_db)
    # TODO HU-10: current_user = Depends(verify_admin)
):
    # TODO: result = OrderControllers.update_order_status(db, order_id, new_status)
    result = None  # placeholder
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Order with id {order_id} not found"
        )
    if result == "locked":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot change status of a delivered order"
        )
    if result == "invalid":
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Invalid order status"
        )
    logger.info(
        f"[{datetime.now()}] Order {order_id} → new status: {new_status}"
    )
    return result
 
 
# ===========================================================================
# REVIEWS
# HU-17 — Publicar reseña → POST /reviews
# HU-18 — Ver reseñas     → GET /albums/{id}/reviews (en router_albums)
# NOTA: no existe tabla reviews en models.py todavía
# TODO: pedir a Naimireth que añada modelo Review
# ===========================================================================
 
@router_reviews.post(
    "/",
    # TODO: response_model=ReviewResponse cuando Maria cree el schema
    status_code=status.HTTP_201_CREATED,
    summary="Publicar reseña",
    description=(
        "Crea una reseña para un álbum. Requiere token. "
        "Body: album_id, puntuacion (1-5), comentario (opcional). "
        "Segunda reseña del mismo user/album devuelve 409. "
        "HU-17."
    )
    # TODO HU-10: añadir Depends(verify_token)
)
def create_review(
    # TODO: review: ReviewCreate cuando Maria cree el schema
    db: Session = Depends(get_db)
    # TODO HU-13: current_user = Depends(verify_token)
):
    # TODO: result = ReviewControllers.create_review(db, review, user_id=current_user.id)
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail="Tabla Review pendiente de Naimireth + schema de Maria + controller de Abel"
    )
 
 
# HU-18 — va en router_albums porque la URL empieza por /albums
@router_albums.get(
    "/{album_id}/reviews",
    # TODO: response_model=ReviewListResponse cuando Maria cree el schema
    status_code=status.HTTP_200_OK,
    summary="Ver reseñas de un álbum (público)",
    description=(
        "Devuelve lista de reseñas + media de puntuación. "
        "Accesible sin token. "
        "HU-18."
    )
)
def get_album_reviews(
    album_id: int,
    db: Session = Depends(get_db)
):
    # TODO: return ReviewControllers.get_reviews(db, album_id)
    # Respuesta debe incluir campo 'average' calculado por Abel
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail="Tabla Review pendiente de Naimireth + controller de Abel"
    )