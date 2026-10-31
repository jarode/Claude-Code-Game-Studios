extends Node2D

const VIEW_SIZE: Vector2 = Vector2(1280.0, 720.0)
const PLAYER_SPEED: float = 390.0
const PLAYER_RADIUS: float = 19.0
const STAR_RADIUS: float = 10.0
const INITIAL_LIVES: int = 3
const ASTEROID_INTERVAL: float = 1.15
const STAR_INTERVAL: float = 1.7
const WHITE: Color = Color(0.91, 0.96, 1.0)
const CYAN: Color = Color(0.24, 0.88, 1.0)
const GOLD: Color = Color(1.0, 0.79, 0.25)
const PINK: Color = Color(1.0, 0.32, 0.48)

var _rng: RandomNumberGenerator = RandomNumberGenerator.new()
var _player_position: Vector2 = VIEW_SIZE * 0.5
var _asteroids: Array[Dictionary] = []
var _stars: Array[Dictionary] = []
var _score: int = 0
var _lives: int = INITIAL_LIVES
var _elapsed: float = 0.0
var _asteroid_clock: float = 0.0
var _star_clock: float = 0.0
var _game_state: StringName = &"title"
var _hurt_flash: float = 0.0
var _starscape: Array[Vector3] = []
var _font: Font


func _ready() -> void:
	_rng.randomize()
	_font = ThemeDB.fallback_font
	for index: int in range(90):
		_starscape.append(Vector3(_rng.randf_range(0.0, VIEW_SIZE.x), _rng.randf_range(0.0, VIEW_SIZE.y), _rng.randf_range(0.35, 1.0)))
	set_process(true)
	queue_redraw()


func _process(delta: float) -> void:
	if _game_state == &"running":
		_update_game(delta)
	elif _hurt_flash > 0.0:
		_hurt_flash = maxf(0.0, _hurt_flash - delta)
	queue_redraw()


func _input(event: InputEvent) -> void:
	if event is InputEventKey and event.pressed and not event.echo:
		if _game_state != &"running" and event.keycode in [KEY_ENTER, KEY_SPACE]:
			_start_game()
		elif event.keycode == KEY_ESCAPE and _game_state == &"running":
			_game_state = &"title"


func _update_game(delta: float) -> void:
	_elapsed += delta
	_asteroid_clock += delta
	_star_clock += delta
	_hurt_flash = maxf(0.0, _hurt_flash - delta)
	var direction: Vector2 = Vector2(
		float(Input.is_key_pressed(KEY_RIGHT) or Input.is_key_pressed(KEY_D)) - float(Input.is_key_pressed(KEY_LEFT) or Input.is_key_pressed(KEY_A)),
		float(Input.is_key_pressed(KEY_DOWN) or Input.is_key_pressed(KEY_S)) - float(Input.is_key_pressed(KEY_UP) or Input.is_key_pressed(KEY_W))
	)
	if direction.length_squared() > 1.0:
		direction = direction.normalized()
	_player_position += direction * PLAYER_SPEED * delta
	_player_position = _player_position.clamp(Vector2(PLAYER_RADIUS + 12.0, 66.0), Vector2(VIEW_SIZE.x - PLAYER_RADIUS - 12.0, VIEW_SIZE.y - PLAYER_RADIUS - 12.0))

	var difficulty: float = 1.0 + _elapsed / 24.0
	var spawn_interval: float = maxf(0.34, ASTEROID_INTERVAL / difficulty)
	while _asteroid_clock >= spawn_interval:
		_asteroid_clock -= spawn_interval
		_spawn_asteroid(difficulty)
	while _star_clock >= STAR_INTERVAL:
		_star_clock -= STAR_INTERVAL
		_spawn_star()

	for index: int in range(_asteroids.size() - 1, -1, -1):
		var asteroid: Dictionary = _asteroids[index]
		var asteroid_position: Vector2 = asteroid["position"] as Vector2
		asteroid_position.y += float(asteroid["speed"]) * delta
		asteroid["position"] = asteroid_position
		_asteroids[index] = asteroid
		if asteroid_position.y - float(asteroid["radius"]) > VIEW_SIZE.y:
			_asteroids.remove_at(index)
		elif _player_position.distance_to(asteroid_position) < PLAYER_RADIUS + float(asteroid["radius"]) * 0.78:
			_asteroids.remove_at(index)
			_lives -= 1
			_hurt_flash = 0.22
			if _lives <= 0:
				_game_state = &"game_over"
				return

	for index: int in range(_stars.size() - 1, -1, -1):
		var star: Dictionary = _stars[index]
		var star_position: Vector2 = star["position"] as Vector2
		star_position.y += float(star["speed"]) * delta
		star["position"] = star_position
		_stars[index] = star
		if _player_position.distance_to(star_position) < PLAYER_RADIUS + STAR_RADIUS:
			_stars.remove_at(index)
			_score += 10
		elif star_position.y > VIEW_SIZE.y + STAR_RADIUS:
			_stars.remove_at(index)


func _spawn_asteroid(difficulty: float) -> void:
	var radius: float = _rng.randf_range(20.0, 38.0)
	_asteroids.append({
		"position": Vector2(_rng.randf_range(radius, VIEW_SIZE.x - radius), -radius),
		"radius": radius,
		"speed": _rng.randf_range(175.0, 255.0) * minf(difficulty, 2.5),
		"spin": _rng.randf_range(-1.5, 1.5),
		"phase": _rng.randf_range(0.0, TAU)
	})


func _spawn_star() -> void:
	_stars.append({"position": Vector2(_rng.randf_range(22.0, VIEW_SIZE.x - 22.0), -STAR_RADIUS), "speed": _rng.randf_range(145.0, 205.0)})


func _start_game() -> void:
	_player_position = VIEW_SIZE * 0.5
	_asteroids.clear()
	_stars.clear()
	_score = 0
	_lives = INITIAL_LIVES
	_elapsed = 0.0
	_asteroid_clock = 0.0
	_star_clock = 0.0
	_game_state = &"running"


func _draw() -> void:
	draw_rect(Rect2(Vector2.ZERO, VIEW_SIZE), Color(0.015, 0.025, 0.08))
	for star: Vector3 in _starscape:
		draw_circle(Vector2(star.x, star.y), star.z * 1.25, Color(0.54, 0.7, 1.0, star.z * 0.5))
	draw_rect(Rect2(Vector2(0.0, 0.0), Vector2(VIEW_SIZE.x, 58.0)), Color(0.035, 0.055, 0.13, 0.92))
	draw_line(Vector2(0.0, 58.0), Vector2(VIEW_SIZE.x, 58.0), Color(0.2, 0.48, 0.7, 0.6), 2.0)
	_draw_text("KOSMICZNY ŁAPACZ", Vector2(30.0, 38.0), 23, CYAN)
	_draw_text("WYNIK  %05d" % _score, Vector2(514.0, 38.0), 22, WHITE)
	_draw_text("ŻYCIA  %s" % "♥ ".repeat(_lives).strip_edges(), Vector2(1034.0, 38.0), 22, PINK if _lives < 3 else WHITE)
	for asteroid: Dictionary in _asteroids:
		_draw_asteroid(asteroid)
	for star: Dictionary in _stars:
		_draw_star(star["position"] as Vector2)
	if _game_state == &"running":
		_draw_ship(_player_position)
		_draw_text("WASD / STRZAŁKI — RUCH", Vector2(30.0, 695.0), 16, Color(0.6, 0.73, 0.9, 0.8))
		_draw_text("ASTEROIDY PRZYŚPIESZAJĄ Z CZASEM", Vector2(827.0, 695.0), 15, Color(0.6, 0.73, 0.9, 0.75))
	elif _game_state == &"title":
		_draw_overlay("KOSMICZNY ŁAPACZ", "Zbieraj gwiazdy i unikaj asteroid", "WASD lub strzałki: ruch  •  ENTER / SPACJA: start", "Naciśnij ENTER, aby rozpocząć")
	elif _game_state == &"game_over":
		_draw_overlay("KONIEC GRY", "Twój wynik: %d" % _score, "WASD lub strzałki: ruch", "ENTER / SPACJA — zagraj ponownie")
	if _hurt_flash > 0.0:
		draw_rect(Rect2(Vector2.ZERO, VIEW_SIZE), Color(1.0, 0.12, 0.22, _hurt_flash * 0.32))


func _draw_overlay(title: String, subtitle: String, controls: String, prompt: String) -> void:
	draw_rect(Rect2(Vector2(250.0, 200.0), Vector2(780.0, 320.0)), Color(0.025, 0.045, 0.11, 0.93))
	draw_rect(Rect2(Vector2(250.0, 200.0), Vector2(780.0, 320.0)), Color(0.17, 0.43, 0.68, 0.9), false, 2.0)
	_draw_text(title, Vector2(0.0, 270.0), 38, CYAN, true)
	_draw_text(subtitle, Vector2(0.0, 326.0), 22, WHITE, true)
	_draw_text(controls, Vector2(0.0, 385.0), 18, Color(0.72, 0.83, 1.0), true)
	_draw_text(prompt, Vector2(0.0, 465.0), 21, GOLD, true)


func _draw_text(text: String, position: Vector2, size: int, color: Color, centered: bool = false) -> void:
	var text_position: Vector2 = position
	if centered:
		text_position.x = (VIEW_SIZE.x - _font.get_string_size(text, HORIZONTAL_ALIGNMENT_LEFT, -1, size).x) * 0.5
	draw_string(_font, text_position, text, HORIZONTAL_ALIGNMENT_LEFT, -1, size, color)


func _draw_ship(position: Vector2) -> void:
	var ship_points: PackedVector2Array = PackedVector2Array([
		position + Vector2(0.0, -PLAYER_RADIUS),
		position + Vector2(PLAYER_RADIUS * 0.78, PLAYER_RADIUS),
		position + Vector2(0.0, PLAYER_RADIUS * 0.55),
		position + Vector2(-PLAYER_RADIUS * 0.78, PLAYER_RADIUS)
	])
	draw_colored_polygon(ship_points, CYAN if _hurt_flash <= 0.0 else WHITE)
	draw_polyline(PackedVector2Array([ship_points[0], ship_points[1], ship_points[2], ship_points[3], ship_points[0]]), WHITE, 2.0, true)
	draw_circle(position, 4.0, Color(0.08, 0.18, 0.38))


func _draw_asteroid(asteroid: Dictionary) -> void:
	var center: Vector2 = asteroid["position"] as Vector2
	var radius: float = float(asteroid["radius"])
	var phase: float = float(asteroid["phase"]) + _elapsed * float(asteroid["spin"])
	var points: PackedVector2Array = PackedVector2Array()
	for index: int in range(9):
		var angle: float = TAU * float(index) / 9.0 + phase
		var point_radius: float = radius * (0.79 + 0.16 * sin(float(index) * 7.1 + phase))
		points.append(center + Vector2(cos(angle), sin(angle)) * point_radius)
	draw_colored_polygon(points, Color(0.46, 0.36, 0.39))
	points.append(points[0])
	draw_polyline(points, Color(0.94, 0.53, 0.56), 2.0, true)


func _draw_star(position: Vector2) -> void:
	var points: PackedVector2Array = PackedVector2Array()
	for index: int in range(10):
		var angle: float = -PI * 0.5 + TAU * float(index) / 10.0
		var radius: float = STAR_RADIUS if index % 2 == 0 else STAR_RADIUS * 0.44
		points.append(position + Vector2(cos(angle), sin(angle)) * radius)
	draw_colored_polygon(points, GOLD)