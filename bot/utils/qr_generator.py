import io, qrcode


def make_qr_bytes(data: str) -> bytes:
    img = qrcode.make(data)
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    bio.seek(0)
    return bio
