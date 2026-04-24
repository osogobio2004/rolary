from django.shortcuts import render
from datetime import date

# Definimos la lista de misiones fuera para poder usarla en varias funciones sin repetir código
CATEGORIAS_MISIONES = [
    {
        'nombre': 'Logros Desbloqueados (Completadas)',
        'misiones': [
            {'titulo': 'Caminar en un parque', 'icono': '🍃'},
            {'titulo': 'Ir a un museo', 'icono': '🏛️'},
            {'titulo': 'Parque acuático', 'icono': '💦'},
            {'titulo': 'Perdernos en una plaza', 'icono': '🏙️'},
            {'titulo': 'Noche de copas/fiesta', 'icono': '🥂'},
            {'titulo': 'Cocinar juntos', 'icono': '🧑‍🍳'},
            {'titulo': 'Pintar un cuadro', 'icono': '🎨'},
            {'titulo': 'Disfrazarnos para Halloween', 'icono': '🎃'},
        ],
        'completada': True
    },
    {
        'nombre': 'Misiones Rápidas (Corto Plazo)',
        'misiones': [
            {'titulo': 'Comprar ropita o cositas a juego', 'icono': '🧸'},
            {'titulo': 'Noche de belleza', 'icono': '🧖‍♀️'},
            {'titulo': 'Maratón de películas/series', 'icono': '🍿'},
            {'titulo': 'Probar algo nuevo (comida/bebida)', 'icono': '🍜'},
            {'titulo': 'Ponernos la ropa del otro', 'icono': '👕'},
            {'titulo': 'Hacer stickers para el álbum', 'icono': '✂️'},
            {'titulo': 'Hacer muñequitos', 'icono': '🧶'},
            {'titulo': 'Pijamada en nuestra primera casita', 'icono': '🏡'},
            {'titulo': 'Ir a un bar/lugar donde toquen en vivo', 'icono': '🎶'},
            {'titulo': 'Ir a una función de teatro', 'icono': '🎭'},
            {'titulo': '24 horas juntos', 'icono': '⏳'},
            {'titulo': 'Cita de adultos xD', 'icono': '🍷'},
            {'titulo': 'Un día en la piscina', 'icono': '🏊‍♀️'},
            {'titulo': 'Aprender a hacer algo nuevo juntos', 'icono': '🧩'},
            {'titulo': 'Un picnic en un parque', 'icono': '🧺'},
            {'titulo': 'Cocinar un rico postre', 'icono': '🧁'},
        ],
        'completada': False
    },
    {
        'nombre': 'Misiones de Exploración (Mediano Plazo)',
        'misiones': [
            {'titulo': 'Ir a la playa', 'icono': '🏖️'},
            {'titulo': 'Ir a un lugar de relajación (Spa)', 'icono': '💆‍♂️'},
            {'titulo': 'Cita elegante', 'icono': '🕯️'},
            {'titulo': 'Visitar un acuario', 'icono': '🐠'},
            {'titulo': 'Llenar todo un álbum de fotos impresas', 'icono': '📸'},
            {'titulo': 'Hacernos un suéter', 'icono': '🧶'},
            {'titulo': 'Ir a un concierto (fuera de Tabasco)', 'icono': '🎸'},
            {'titulo': 'Ir a un lugar de senderismo', 'icono': '🥾'},
            {'titulo': 'Ir a un río', 'icono': '🛶'},
            {'titulo': 'Salir de viaje fuera del estado', 'icono': '🚗'},
            {'titulo': 'Acampar', 'icono': '⛺'},
            {'titulo': 'Visitar un pueblito mágico', 'icono': '🏘️'},
            {'titulo': 'Ir al centro histórico de Guanajuato/Morelia', 'icono': '⛪'},
            {'titulo': 'Viaje de carretera con música', 'icono': '🛣️'},
            {'titulo': 'Regalarnos cartitas en nuestros aniversarios (14-may)', 'icono': '💌'},
        ],
        'completada': False
    },
    {
        'nombre': 'Historia Principal (Largo Plazo)',
        'misiones': [
            {'titulo': 'Recorrer el país', 'icono': '🇲🇽'},
            {'titulo': 'Salir del país', 'icono': '✈️'},
            {'titulo': 'Tener nuestro propio jardín', 'icono': '🪴'},
            {'titulo': 'Toda una vida juntos', 'icono': '♾️'},
            {'titulo': 'Casarnos', 'icono': '💍'},
            {'titulo': 'Decorar nuestra casa', 'icono': '🛋️'},
            {'titulo': 'Dejar a nuestro hijo en su primer día de kinder', 'icono': '🎒'},
            {'titulo': 'Hacer el primer súper para nuestra casita', 'icono': '🛒'},
        ],
        'completada': False
    }
]

def dashboard(request):
    fecha_inicio = date(2025, 5, 14) 
    hoy = date.today()
    dias_juntos = (hoy - fecha_inicio).days

    context = {
        'dias_juntos': dias_juntos,
        'categorias': CATEGORIAS_MISIONES, # <-- Ahora sí el dashboard tiene las misiones
    }
    return render(request, 'savefile/dashboard.html', context)

def misiones(request):
    return render(request, 'savefile/misiones.html', {'categorias': CATEGORIAS_MISIONES})

def recuerdos(request):
    lista_recuerdos = [
        {'titulo': 'Espacio guardado para recuerdos', 'fecha': 'Próximamente', 'descripcion': 'Aquí guardaremos nuestros mejores momentos.', 'emoji': '💭'},
    ]
    return render(request, 'savefile/recuerdos.html', {'recuerdos': lista_recuerdos})