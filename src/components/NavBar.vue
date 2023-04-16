<script setup>
import VueLogo from "./icons/VueLogo.vue"
import GithubLogo from "./icons/GithubLogo.vue"
defineProps(["isLoading", "postAction", "btnStatus", "renderHtml"])
</script>

<template>
    <header>
        <nav class="container">
            <ul>
                <li>
                    <button class="outline" :aria-busy="isLoading" @click="">
                        AyaMark
                    </button>
                </li>
                <li>
                    <button :class="btnStatus" @click="renderHtml">Render</button>
                </li>
            </ul>
            <ul>
                <li>
                    <a href="https://github.com/Xyaya/ayaclip" target="_blank">
                        <GithubLogo />
                    </a>
                </li>
            </ul>
        </nav>
    </header>
</template>

<style scoped>
header {
    position: fixed;
    width: 100%;
    top: 0;
    background-color: white;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
}
</style>