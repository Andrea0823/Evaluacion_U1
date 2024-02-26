CREATE TABLE usuarios (
    id_usuario INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    password TEXT NOT NULL,
    rol TEXT NOT NULL,
    status TEXT NOT NULL,
    fecha_actualizacion TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE privilegios (
    id_privilegio INTEGER PRIMARY KEY,
    privilegio TEXT NOT NULL,
    descripcion TEXT NOT NULL
);
CREATE TABLE tablas (
    id_tabla INT PRIMARY KEY,
    tabla TEXT NOT NULL,
    descripcion TEXT NOT NULL
);
CREATE TABLE productos (
    id_producto INT PRIMARY KEY,
    producto TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    precio TEXT NOT NULL    
);


CREATE TABLE usuarios_privilegios_tablas (
	id_usuarios_privilegios_tablas INTEGER PRIMARY KEY,
    id_usuario INTEGER,
    id_privilegio INTEGER,
    id_tabla INTEGER,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_privilegio) REFERENCES privilegios(id_privilegio),
    FOREIGN KEY (id_tabla) REFERENCES tablas(id_tabla)
);


