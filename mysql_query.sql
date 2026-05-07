SELECT 
    f.film_id AS ID,
    f.title AS MOVIE_TITLE,
    cat.name AS GENRE,
    f.rental_rate AS UNIT_PRICE,
    -- Isolated Calculations (The only way to avoid the 11,22 issue)
    (SELECT COUNT(r.rental_id) 
     FROM rental r 
     JOIN inventory i ON r.inventory_id = i.inventory_id 
     WHERE i.film_id = f.film_id) AS TOTAL_RENTALS,
     
    (SELECT SUM(p.amount) 
     FROM payment p 
     JOIN rental r2 ON p.rental_id = r2.rental_id 
     JOIN inventory i2 ON r2.inventory_id = i2.inventory_id 
     WHERE i2.film_id = f.film_id) AS TOTAL_REVENUE,
     
    (SELECT COUNT(*) 
     FROM inventory i3 
     WHERE i3.film_id = f.film_id) AS CURRENT_STOCK,
     
    -- Location Data (Using LIMIT 1 to prevent row doubling)
    (SELECT co.country 
     FROM inventory i4 
     JOIN store s ON i4.store_id = s.store_id 
     JOIN address ad ON s.address_id = ad.address_id 
     JOIN city ci ON ad.city_id = ci.city_id 
     JOIN country co ON ci.country_id = co.country_id 
     WHERE i4.film_id = f.film_id LIMIT 1) AS REGION,
     
    (SELECT ad.address 
     FROM inventory i5 
     JOIN store s ON i5.store_id = s.store_id 
     JOIN address ad ON s.address_id = ad.address_id 
     WHERE i5.film_id = f.film_id LIMIT 1) AS STORE_LOCATION

FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category cat ON fc.category_id = cat.category_id
ORDER BY f.film_id ASC;
