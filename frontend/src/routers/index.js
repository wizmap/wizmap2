import { createWebHistory, createRouter } from "vue-router";
import Login from "../components/Login.vue";
import Home from "../components/Home.vue";
import Search from "../components/Search.vue";
import SearchResult from "../components/SearchResult.vue";
import SearchFavorite from "../components/SearchFavorite.vue";
import SearchHistory from "../components/SearchHistory.vue";

const router = createRouter({
    history : createWebHistory(),
    routes : [ // path별 component를 추가한다.
        { path : "/", name : "home", component : Home },
        {
            path: "/search",  // Search.vue로 이동할 Path
            name: "Search",  // router name
            component: Search,  // Path로 이동될 Component
        },
        {
            path: "/searchresult",  
            name: "SearchResult",  
            component: SearchResult,
        },
        {
            path: "/favorites",
            name: "Favorites",
            component: SearchFavorite,
            meta: { requiresAuth: true } 
        },
        {
            path: "/history",
            name: "SearchHistory",
            component: SearchHistory,
            meta: { requiresAuth: true } 
        },
    ]
});

router.beforeEach((to, from, next) => {
    const isLoggedIn = localStorage.getItem('userToken') // 로그인 상태 확인
    if (to.matched.some(record => record.meta.requiresAuth) && !isLoggedIn) {
        // 인증이 필요한 페이지에 접근하려고 할 때 로그인되어있지 않다면 searchresult 페이지로 이동
        next('/searchresult')
    } else {
        next()
    }
});

export default router;

