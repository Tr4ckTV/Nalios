SELECT p.name
FROM products p
JOIN product_categories pc ON p.id = pc.product_id
JOIN categories c ON pc.category_id = c.id
WHERE c.is_private = FALSE
GROUP BY p.id
HAVING COUNT(DISTINCT c.id) > 5;