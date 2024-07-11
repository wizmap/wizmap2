import { createWebHistory, createRouter } from "vue-router";
import SearchResult from "../components/SearchResult.vue";
import Home from "../components/Home.vue";
<<<<<<< HEAD
import SearchFavorite from "../components/SearchFavorite.vue";

=======
import SearchHistory from "../components/SearchHistory.vue";
>>>>>>> ee426d85970b5385f458401588e2485e161fd105

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
<<<<<<< HEAD
            path: "/favorites",
            name: "Favorites",
            component: SearchFavorite,
=======
            path: "/history",
            name: "SearchHistory",
            component: SearchHistory,
>>>>>>> ee426d85970b5385f458401588e2485e161fd105
        },
    ]
});

export default router;

