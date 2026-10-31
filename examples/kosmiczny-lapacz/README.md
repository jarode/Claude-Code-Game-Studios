# Kosmiczny Łapacz

Mała, samodzielna gra 2D w Godot 4. Steruj statkiem, zbieraj gwiazdy (+10 pkt)
i unikaj asteroid. Masz trzy życia; tempo pojawiania się i prędkość asteroid
rosną w trakcie rozgrywki. Grafika jest rysowana proceduralnie, bez zewnętrznych
zasobów.

## Uruchomienie

Otwórz ten katalog w Godot 4 i uruchom projekt albo z terminala:

```sh
godot --path examples/kosmiczny-lapacz
```

## Sterowanie

- **WASD** lub **strzałki** — ruch statku
- **Enter** lub **Spacja** — start i ponowna gra
- **Esc** — powrót do ekranu tytułowego

Widok gry ma rozdzielczość 1280×720.

## Lekki test struktury

```sh
python3 -m unittest discover -s examples/kosmiczny-lapacz/tests
```