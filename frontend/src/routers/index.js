import { createWebHistory, createRouter } from "vue-router";
import SearchResult from "../components/SearchResult.vue";
import Home from "../components/Home.vue";
import SearchFavorite from "../components/SearchFavorite.vue";

import SearchHistory from "../components/SearchHistory.vue";

const router = createRouter({
    history : createWebHistory(),
    routes : [ // path별 component를 추가한다.
        { path : "/", name : "home", component : Home },
        {
            path: "/search",  // TestComponent.vue로 이동할 Path
            name: "SearchResult",  // router name
            component: SearchResult,  // Path로 이동될 Component
        },
        {
            path: "/favorites",
            name: "Favorites",
            component: SearchFavorite,
        },
        {
            path: "/history",
            name: "SearchHistory",
            component: SearchHistory,
        },
    ]
});

export default router;

