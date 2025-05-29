#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

using namespace std;

struct Pokemon {
    string nombre;
    int vida;
    int energia;
    int ataque;
    int poderEspecial;
    int terremoto;

    void mostrarEstado() {
        cout << nombre << " | Vida: " << vida << " | Energía: " << energia << endl;
    }
};

void atacar(Pokemon &atacante, Pokemon &objetivo) {
    if (atacante.energia >= 10) {
        cout << atacante.nombre << " ataca a " << objetivo.nombre << " causando " << atacante.ataque << " de daño.\n";
        objetivo.vida -= atacante.ataque;
        atacante.energia -= 10;
    } else {
        cout << atacante.nombre << " no tiene suficiente energía para atacar.\n";
    }
}

void movimientoEspecial(Pokemon &atacante, Pokemon &objetivo) {
    if (atacante.energia >= 20) {
        cout << atacante.nombre << " usa su movimiento especial contra " << objetivo.nombre << ", causando " << atacante.poderEspecial << " de daño.\n";
        objetivo.vida -= atacante.poderEspecial;
        atacante.energia -= 20;
    } else {
        cout << atacante.nombre << " no tiene suficiente energía para su movimiento especial.\n";
    }
}

void usarTerremoto(Pokemon &atacante, Pokemon &objetivo) {
    if (atacante.energia >= 15) {
        cout << atacante.nombre << " usa Terremoto contra " << objetivo.nombre << ", causando " << atacante.terremoto << " de daño.\n";
        objetivo.vida -= atacante.terremoto;
        atacante.energia -= 15;
    } else {
        cout << atacante.nombre << " no tiene suficiente energía para usar Terremoto.\n";
    }
}

void recuperarEnergia(Pokemon &pokemon) {
    pokemon.energia += 5;
    if (pokemon.energia > 100) pokemon.energia = 100;
}

int main() {
    srand(time(0)); // Inicializar aleatoriedad

    Pokemon jugador = {"Pikachu", 100, 50, 20, 30, 10};
    Pokemon oponente = {"Charmander", 100, 50, 15, 30, 10};

    int turno = 1;

    while (jugador.vida > 0 && oponente.vida > 0) {
        cout << "\n--- Turno " << turno << " ---\n";
        jugador.mostrarEstado();
        oponente.mostrarEstado();

        // Turno del jugador
        cout << "\nTu turno. Elige una acción:\n";
        cout << "1. Atacar\n2. Pasar turno\n3. Movimiento Especial\n4. Terremoto\n> ";
        int opcion;
        cin >> opcion;

        if (opcion == 1) {
            atacar(jugador, oponente);
        } else if (opcion == 2) {
            cout << jugador.nombre << " ha decidido pasar turno...\n";
        } else if (opcion == 3) {
            movimientoEspecial(jugador, oponente);
        } else if (opcion == 4) {
            usarTerremoto(jugador, oponente);
        } else {
            cout << "Opción inválida. Pierdes el turno.\n";
        }

        recuperarEnergia(jugador);
        if (oponente.vida <= 0) break;

        // Turno del oponente (versión simplificada)
        cout << "\nTurno del oponente...\n";
        int eleccion = rand() % 3; // 0 = especial, 1 = ataque, 2 = esperar

        if (eleccion == 0 && oponente.energia >= 20) {
            movimientoEspecial(oponente, jugador);
        } else if (eleccion == 1 && oponente.energia >= 10) {
            atacar(oponente, jugador);
        } else {
            cout << oponente.nombre << " decide esperar...\n";
        }

        recuperarEnergia(oponente);
        turno++;
    }

    // Resultado del combate
    cout << "\n--- Fin del combate ---\n";
    if (jugador.vida <= 0)
        cout << jugador.nombre << " ha sido derrotado. ¡Perdiste!\n";
    else
        cout << oponente.nombre << " ha sido derrotado. ¡Ganaste!\n";

    return 0;
}