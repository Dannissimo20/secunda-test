-- Заполнение таблицы Activity
INSERT INTO activities (id, name, parent_id, level) VALUES
('931c5f5b-8d24-42f0-89f8-ed316641cb19', 'Еда', NULL, 1),
('f9ce3e49-2f3f-4d3f-bf9f-8ec895c87a10', 'Автомобили', NULL, 1),
('c29013b2-3763-4c77-8b80-027ab578352c', 'Мясная продукция', '931c5f5b-8d24-42f0-89f8-ed316641cb19', 2),
('dce53d42-ff0b-42d4-8620-303b9d55ab99', 'Молочная продукция', '931c5f5b-8d24-42f0-89f8-ed316641cb19', 2),
('f2b23710-38cf-4aeb-9660-a009b769a5ff', 'Грузовые', 'f9ce3e49-2f3f-4d3f-bf9f-8ec895c87a10', 2),
('2cea7333-6ee1-4a86-9701-b61bbc12fcf8', 'Легковые', 'f9ce3e49-2f3f-4d3f-bf9f-8ec895c87a10', 2),
('d724fa02-0860-4ce0-b10f-8abb9e03e45c', 'Запчасти', '2cea7333-6ee1-4a86-9701-b61bbc12fcf8', 3),
('863605e1-f4b2-4228-8a8e-6e6f7a838a65', 'Аксессуары', '2cea7333-6ee1-4a86-9701-b61bbc12fcf8', 3);

-- Заполнение таблицы buildings
INSERT INTO buildings (id, address, latitude, longitude) VALUES
('dbfe80fa-cb2b-46e3-95c5-998ab752608c', 'Блюхера, 32/1', 61.28659600, 30.24713000),
('d2fb8d18-c120-49bc-8885-f95fe1ee0820', 'г. Санкт-петербург, ул. Дворцовая наб., д. 32', 59.94027778, 30.31388889);

-- Заполнение таблицы organizations
INSERT INTO organizations (id, name, phone, building_id) VALUES
('e8fcc764-7206-464a-b6ac-90f5c1b4cc58', 'ООО "Рога и Копыта"', '{"2-222-222","8-923-666-13-13"}', 'dbfe80fa-cb2b-46e3-95c5-998ab752608c'),
('2045375c-0cf6-45af-8432-abb2df53ef27', 'ООО "Покупаем Продаем"', '{"999-999","89999999999"}', 'dbfe80fa-cb2b-46e3-95c5-998ab752608c'),
('cfe885dd-52c9-4b93-873f-a5658c2cb1ef', 'ООО "Красивое"', '{"999-345"}', 'd2fb8d18-c120-49bc-8885-f95fe1ee0820');

-- Заполнение таблицы organization_activities
INSERT INTO organization_activities (organization_id, activity_id) VALUES
('2045375c-0cf6-45af-8432-abb2df53ef27', '931c5f5b-8d24-42f0-89f8-ed316641cb19'),
('2045375c-0cf6-45af-8432-abb2df53ef27', 'd724fa02-0860-4ce0-b10f-8abb9e03e45c'),
('cfe885dd-52c9-4b93-873f-a5658c2cb1ef', 'f2b23710-38cf-4aeb-9660-a009b769a5ff'),
('e8fcc764-7206-464a-b6ac-90f5c1b4cc58', '2cea7333-6ee1-4a86-9701-b61bbc12fcf8');