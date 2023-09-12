/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { GetTasksResponse } from '../models/GetTasksResponse';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class TasksService {

    /**
     * Get Tasks
     * @returns GetTasksResponse Successful Response
     * @throws ApiError
     */
    public static getTasks(): CancelablePromise<GetTasksResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/tasks',
        });
    }

}
