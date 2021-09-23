package ru.gb.whatseat.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import ru.gb.whatseat.entity.byUser.UserEntity;

import java.util.Optional;
import java.util.UUID;

@Repository
public interface UserRepository extends JpaRepository<UserEntity, UUID> {
    UserEntity findByLogin(String login);
    Optional<UserEntity> findById(UUID uuid);
}
