@@ -0,0 +1,55 @@
CREATE TABLE `Rides` (
  `id` int NOT NULL AUTO_INCREMENT,
  `driver_id` int DEFAULT NULL,
  `ride_date` date DEFAULT NULL,
  `start_time` time DEFAULT NULL,
  `passengers_num` int DEFAULT NULL,
  `price` decimal(15,2) DEFAULT NULL,
  `animals` tinyint(1) DEFAULT NULL,
  `freeText` char(100) DEFAULT NULL,
  `pas1` int DEFAULT NULL,
  `pas2` int DEFAULT NULL,
  `pas3` int DEFAULT NULL,
  `pas4` int DEFAULT NULL,
  `startPoint` char(50) NOT NULL,
  `endPoint` char(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Rides_users_id_fk` (`driver_id`),
  KEY `Rides_users_id_fk_2` (`pas1`),
  KEY `Rides_users_id_fk_3` (`pas2`),
  KEY `Rides_users_id_fk_4` (`pas3`),
  KEY `Rides_users_id_fk_5` (`pas4`),
  CONSTRAINT `rides_ibfk_1` FOREIGN KEY (`driver_id`) REFERENCES `users` (`id`),
  CONSTRAINT `Rides_users_id_fk` FOREIGN KEY (`driver_id`) REFERENCES `users` (`id`),
  CONSTRAINT `Rides_users_id_fk_2` FOREIGN KEY (`pas1`) REFERENCES `users` (`id`),
  CONSTRAINT `Rides_users_id_fk_3` FOREIGN KEY (`pas2`) REFERENCES `users` (`id`),
  CONSTRAINT `Rides_users_id_fk_4` FOREIGN KEY (`pas3`) REFERENCES `users` (`id`),
  CONSTRAINT `Rides_users_id_fk_5` FOREIGN KEY (`pas4`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` char(30) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` char(30) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `psw` char(30) NOT NULL,
  `file` char(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci



INSERT INTO group7.users (name, email, phone, birthday, psw, file) VALUES ('sami', 'de@gn.co', '0578978977', '2015-08-10', '123', null);
INSERT INTO group7.users (name, email, phone, birthday, psw, file) VALUES ('somo', 'email@vf.vf', '0524782194', '1989-08-17', '123123', null);
INSERT INTO group7.users (name, email, phone, birthday, psw, file) VALUES ('ariel', 'm@g.com', '0522222222', '1989-06-14', '123123', null);
INSERT INTO group7.users (name, email, phone, birthday, psw, file) VALUES ('עמרי', 'om@gmail.com', '0544879528', '1992-11-22', 'edwde!Efr1', null);
INSERT INTO group7.users (name, email, phone, birthday, psw, file) VALUES ('רועי', 'roi@gmail.com', '0525564248', '1994-11-09', '12332144', null);

INSERT INTO group7.Rides (driver_id, ride_date, start_time, passengers_num, price, animals, freeText, pas1, pas2, pas3, pas4, startPoint, endPoint) VALUES (3, '2022-08-03', '10:00:00', 2, 20.00, 0, null, 1, 2, null, null, 'באר שבע', 'תל אביב');
INSERT INTO group7.Rides (driver_id, ride_date, start_time, passengers_num, price, animals, freeText, pas1, pas2, pas3, pas4, startPoint, endPoint) VALUES (1, '2022-05-01', '20:15:00', 4, 25.00, 0, null, 5, 3, 2, 4, 'ירושלים', 'באר שבע');
INSERT INTO group7.Rides (driver_id, ride_date, start_time, passengers_num, price, animals, freeText, pas1, pas2, pas3, pas4, startPoint, endPoint) VALUES (4, '2022-08-31', '18:30:00', 3, 50.00, 1, null, 2, 5, 1, null, 'באר שבע', 'חיפה');



