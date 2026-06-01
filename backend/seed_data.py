# seed_data.py

from database.database import LocalSession
from sqlalchemy.orm import Session
from models.musintage_models import Artist, Genre, FormatType

def seed_artists(db: Session):
    """Popular tabla de artistas"""
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
    
    for artist_data in artists:
        # Verificar si ya existe
        existing = db.query(Artist).filter(Artist.name == artist_data["name"]).first()
        if not existing:
            artist = Artist(**artist_data)
            db.add(artist)
            print(f"✓ Añadido artista: {artist_data['name']}")
    
    db.commit()
    print(f"✅ Total artistas insertados/actualizados: {len(artists)}")

def seed_genres(db: Session):
    """Popular tabla de géneros"""
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
    
    for genre_data in genres:
        # Verificar si ya existe
        existing = db.query(Genre).filter(Genre.name == genre_data["name"]).first()
        if not existing:
            genre = Genre(**genre_data)
            db.add(genre)
            print(f"✓ Añadido género: {genre_data['name']}")
    
    db.commit()
    print(f"✅ Total géneros insertados/actualizados: {len(genres)}")

def seed_format_types(db: Session):
    """Popular tabla de tipos de formato"""
    formats = [
        {"name": "Vinilo"},
        {"name": "Cassette"},
        {"name": "CD"},
        {"name": "Digital"}
    ]
    
    for format_data in formats:
        # Verificar si ya existe
        existing = db.query(FormatType).filter(FormatType.name == format_data["name"]).first()
        if not existing:
            format_type = FormatType(**format_data)
            db.add(format_type)
            print(f"✓ Añadido formato: {format_data['name']}")
    
    db.commit()
    
    # Mostrar los formatos con sus IDs
    all_formats = db.query(FormatType).all()
    print(f"✅ Total formatos insertados/actualizados: {len(formats)}")
    print("\n📋 IDs de formatos disponibles:")
    for f in all_formats:
        print(f"   ID {f.id}: {f.name}")

def main():
    print("🌱 Iniciando seeding de base de datos...")
    print("=" * 50)
    
    db = LocalSession()
    try:
        seed_artists(db)
        print("-" * 40)
        seed_genres(db)
        print("-" * 40)
        seed_format_types(db)
        print("=" * 50)
        print("\n✨ Seeding completado exitosamente!")
    except Exception as e:
        print(f"❌ Error durante el seeding: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()