# database/seed.py

from database.database import LocalSession
from sqlalchemy.orm import Session
from models.musintage_models import Artist, Genre, FormatType
import logging

logger = logging.getLogger(__name__)

def seed_artists(db: Session):
    artists = [
        {"name": "Michael Jackson", "nationality": "American"},
        {"name": "Madonna", "nationality": "American"},
        {"name": "Prince", "nationality": "American"},
        {"name": "Whitney Houston", "nationality": "American"},
        {"name": "U2", "nationality": "Irish"},
        {"name": "Guns N' Roses", "nationality": "American"},
        {"name": "Nirvana", "nationality": "American"},
        {"name": "Pearl Jam", "nationality": "American"},
        {"name": "Metallica", "nationality": "American"},
        {"name": "Bon Jovi", "nationality": "American"},
        {"name": "Depeche Mode", "nationality": "British"},
        {"name": "The Cure", "nationality": "British"},
        {"name": "R.E.M.", "nationality": "American"},
        {"name": "Red Hot Chili Peppers", "nationality": "American"},
        {"name": "Smashing Pumpkins", "nationality": "American"},
        {"name": "Oasis", "nationality": "British"},
        {"name": "Alanis Morissette", "nationality": "Canadian"},
        {"name": "Mariah Carey", "nationality": "American"},
        {"name": "TLC", "nationality": "American"},
        {"name": "Soundgarden", "nationality": "American"}
    ]
    added = 0
    for data in artists:
        if not db.query(Artist).filter(Artist.name == data["name"]).first():
            db.add(Artist(**data))
            added += 1
    db.commit()
    logger.info(f"✓ Artistas: {added} nuevos / {len(artists)} totales")
    return added

def seed_genres(db: Session):
    genres = [
        {"name": "Pop"},
        {"name": "Pop / Rock"},
        {"name": "Pop / R&B"},
        {"name": "Pop / R&B / Soundtrack"},
        {"name": "Rock"},
        {"name": "Hard Rock"},
        {"name": "Grunge / Rock"},
        {"name": "Thrash Metal"},
        {"name": "Heavy Metal"},
        {"name": "Synth-pop"},
        {"name": "Alternative Rock"},
        {"name": "Post-punk / Gothic Rock"},
        {"name": "Funk Rock"},
        {"name": "Britpop"},
        {"name": "Pop / Ballad"},
        {"name": "R&B / Hip Hop"},
        {"name": "Grunge"}
    ]
    added = 0
    for data in genres:
        if not db.query(Genre).filter(Genre.name == data["name"]).first():
            db.add(Genre(**data))
            added += 1
    db.commit()
    logger.info(f"✓ Géneros: {added} nuevos / {len(genres)} totales")
    return added

def seed_format_types(db: Session):
    formats = [
        {"name": "Vinilo"},
        {"name": "Cassette"},
        {"name": "CD"},
        {"name": "Digital"}
    ]
    added = 0
    for data in formats:
        if not db.query(FormatType).filter(FormatType.name == data["name"]).first():
            db.add(FormatType(**data))
            added += 1
    db.commit()
    logger.info(f"✓ Formatos: {added} nuevos / {len(formats)} totales")
    return added

def run_seed():
    logger.info("🌱 Iniciando seeding...")
    db = LocalSession()
    try:
        a = seed_artists(db)
        g = seed_genres(db)
        f = seed_format_types(db)
        total = a + g + f
        if total == 0:
            logger.info("✅ BD ya poblada")
        else:
            logger.info(f"✨ Seeding completado: {total} registros nuevos")
        return True
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        db.rollback()
        return False
    finally:
        db.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run_seed()